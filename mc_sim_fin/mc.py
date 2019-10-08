import mc_sim_fin.utils.helpers as helpers
from pandas import Series
from typing import Dict, Tuple


def mc_analysis(result_dates: Series, result_amounts: Series, start_equity: float,
                ruin_equity: float, sim_years_duration=1, nb_sims=10000):

    nb_trades_for_sample = helpers.comp_nb_trades_for_sample(result_dates, sim_years_duration)

    sims = run_simulations(nb_sims, nb_trades_for_sample, result_amounts, start_equity, ruin_equity)

    return get_simulations_results(sims, start_equity)


def run_simulations(nb_sims: int, nb_trades_for_sample: int, result_amounts: Series, start_equity: float,
                    ruin_equity: float) -> Tuple:
    sims_drawdown, sims_profit, sims_is_positive_profit, sims_is_ruin = [], [], [], []

    for i in range(0, nb_sims):
        randomized_trade_results = helpers.get_randomized_trade_results(result_amounts, nb_trades_for_sample)
        sims_drawdown.append(helpers.get_abs_max_drawdown(randomized_trade_results))
        sims_profit.append(helpers.get_profit(randomized_trade_results))
        sims_is_positive_profit.append(helpers.is_sim_returns_positive(randomized_trade_results))
        sims_is_ruin.append(helpers.is_sim_ruin(randomized_trade_results, start_equity, ruin_equity))

    return {'is_ruin': sims_is_ruin, 'drawdown': sims_drawdown, 'profit': sims_profit, 'is_profit_positive': sims_is_positive_profit}


def get_simulations_results(sims, start_equity: float) -> Dict:

    risk_of_ruin_percent = helpers.get_sims_ruin_probability_percent(sims['is_ruin'])
    med_drawdown_percent = helpers.get_sims_median_drawdown_percent(sims['drawdown'], start_equity)
    med_profit_percent = helpers.get_sims_median_return_percent(sims['profit'], start_equity)
    prob_profit_is_positive = helpers.get_sims_return_positive_percent(sims['is_profit_positive'])

    return {'risk_of_ruin_percent': risk_of_ruin_percent,
            'med_drawdown_percent': med_drawdown_percent,
            'med_profit_percent': med_profit_percent,
            'prob_profit_is_positive': prob_profit_is_positive}
