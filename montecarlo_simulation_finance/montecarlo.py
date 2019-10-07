from pandas import Series
from typing import Tuple
import montecarlo_simulation_finance.utils as utils


def mc_sims(result_dates: Series, result_amounts: Series, start_equity: float,
            ruin_equity: float, sim_years_duration=1, nb_sims=10000):

    nb_trades_result = utils.get_nb_trades(result_dates)
    nb_years_result = utils.get_duration_in_years(result_dates)
    avg_trades_per_year_result = utils.get_avg_trades_per_year(nb_trades_result, nb_years_result)
    nb_trades_for_sample = utils.get_nb_trades_for_sample(avg_trades_per_year_result, sim_years_duration)
    sim_drawdowns, sim_returns, sim_positive_returns, sim_is_ruin = make_simulations(nb_sims, nb_trades_for_sample,
                                                                                     result_amounts, start_equity, ruin_equity)

    risk_of_ruin_percent, med_drawdown_percent, med_return_percent, prob_returns_positive = get_simulations_results(sim_drawdowns,
                                                                                                                    sim_returns,
                                                                                                                    sim_positive_returns,
                                                                                                                    sim_is_ruin,
                                                                                                                    start_equity)

    return {'risk_of_ruin_percent': risk_of_ruin_percent,
            'med_drawdown_percent': med_drawdown_percent,
            'med_return_percent': med_return_percent,
            'prob_returns_positive': prob_returns_positive}


def make_simulations(nb_sims: int, nb_trades_for_sample: int, result_amounts: Series, start_equity: float,
                     ruin_equity: float) -> Tuple:
    sim_drawdowns, sim_profit, sim_positive_profit, sim_is_ruin = [], [], [], []

    for i in range(0, nb_sims):
        randomized_trade_results = utils.get_randomized_trade_results(result_amounts, nb_trades_for_sample)
        sim_drawdowns.append(utils.get_abs_max_drawdown(randomized_trade_results))
        sim_profit.append(utils.get_profit(randomized_trade_results))
        sim_positive_profit.append(utils.is_sim_returns_positive(randomized_trade_results))
        sim_is_ruin.append(utils.is_sim_ruin(randomized_trade_results, start_equity, ruin_equity))

    return sim_drawdowns, sim_profit, sim_positive_profit, sim_is_ruin


def get_simulations_results(sim_drawdowns: list, sim_profit: list, sim_positive_profit: list, sim_is_ruin: list, start_equity: float) -> Tuple:

    risk_of_ruin_percent = utils.get_sims_ruin_probability_percent(sim_is_ruin)
    med_drawdown_percent = utils.get_sims_median_drawdown_percent(sim_drawdowns, start_equity)
    med_return_percent = utils.get_sims_median_return_percent(sim_profit, start_equity)
    prob_returns_positive = utils.get_sims_return_positive_percent(sim_positive_profit)

    return risk_of_ruin_percent, med_drawdown_percent, med_return_percent, prob_returns_positive
