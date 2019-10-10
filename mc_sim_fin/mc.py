import mc_sim_fin.utils.helpers as helpers
from typing import Dict, Tuple
from pandas import DataFrame


def mc_analysis(results: DataFrame, start_equity: float,
                ruin_equity: float, **kwargs):

    date_results, profit_results = helpers.extract_date_profit_columns(results)
    sim_years_duration, nb_iterations = helpers.extract_extra_params(kwargs)

    nb_trades_for_sample = helpers.comp_nb_trades_for_sample(date_results, sim_years_duration)

    iter_params = {'nb_trades_for_sample': nb_trades_for_sample,
                   'profit_results': profit_results,
                   'start_equity': start_equity,
                   'ruin_equity': ruin_equity}

    sim = run_simulation(iter_params, nb_iterations)

    return get_simulation_results(sim, start_equity)


def run_simulation(iter_params: Tuple, nb_iterations: int) -> Tuple:
    sim_drawdown, sim_profit, sim_is_positive_profit, sim_is_ruin = [], [], [], []

    for _ in range(0, nb_iterations):
        randomized_trade_results = helpers.get_randomized_trade_results(iter_params['profit_results'], iter_params['nb_trades_for_sample'])
        sim_is_ruin.append(helpers.is_iteration_ruin(randomized_trade_results, iter_params['start_equity'], iter_params['ruin_equity']))
        sim_drawdown.append(helpers.get_abs_max_drawdown(randomized_trade_results))
        sim_profit.append(helpers.get_profit(randomized_trade_results))
        sim_is_positive_profit.append(helpers.is_iteration_returns_positive(randomized_trade_results))

    return {'is_ruin': sim_is_ruin, 'drawdown': sim_drawdown, 'profit': sim_profit, 'is_profit_positive': sim_is_positive_profit}


def get_simulation_results(sim, start_equity: float) -> Dict:

    risk_of_ruin_percent = helpers.get_sim_ruin_probability_percent(sim['is_ruin'])
    med_max_drawdown_percent = helpers.get_sim_median_drawdown_percent(sim['drawdown'], start_equity)
    med_profit_percent = helpers.get_sim_median_return_percent(sim['profit'], start_equity)
    prob_profit_is_positive = helpers.get_sim_return_positive_percent(sim['is_profit_positive'])

    return {'risk_of_ruin_percent': risk_of_ruin_percent,
            'med_max_drawdown_percent': med_max_drawdown_percent,
            'med_profit_percent': med_profit_percent,
            'prob_profit_is_positive': prob_profit_is_positive}
