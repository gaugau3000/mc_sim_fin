from mc_sim_fin.mc import mc_analysis
import mc_sim_fin.utils.helpers as helpers
import pandas as pd
import numpy as np
from datetime import datetime


def test_2_trades_per_year_with_1_year_simulation_should_use_2_samples_for_simulation():

    date_results = pd.Series([datetime(2018, 1, 1), datetime(2018, 12, 31)])
    nb_samples_simulation = helpers.comp_nb_trades_for_sample(date_results, 1)
    assert nb_samples_simulation == 2


def test_start_equity_5000_ruin_equity_4000_1_year_test():
    date_results = pd.date_range(start='1/1/2017', end='31/12/2017').tolist()
    profit_results = np.resize([200, -150], 365)

    results = pd.DataFrame({'date_results': date_results, 'profit_results': profit_results})

    mc_sims_results = mc_analysis(results=results, start_equity=5000, ruin_equity=4000, sim_years_duration=1, nb_iterations=10000)

    assert 0.13 < mc_sims_results['risk_of_ruin_percent'] < 0.18
    assert 0.33 < round(mc_sims_results['med_max_drawdown_percent'], 2) < 0.37
    assert 1.80 < mc_sims_results['med_profit_percent'] < 2.00
    assert mc_sims_results['prob_profit_is_positive'] > 0.996

    # print(mc_sims_results)
