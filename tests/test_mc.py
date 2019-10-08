from mc_sim_fin.mc import mc_analysis
import pandas as pd
import numpy as np


def test_start_equity_5000_ruin_equity_4000_1_year_test():
    result_dates = pd.date_range(start='1/1/2017', end='31/12/2017').tolist()
    result_amounts = np.resize([200, -150], 365)

    df = pd.DataFrame({'result_dates': result_dates, 'result_amounts': result_amounts})

    mc_sims_results = mc_analysis(df['result_dates'], df['result_amounts'], 5000, 4000, 1, 10000)

    assert 0.13 < mc_sims_results['risk_of_ruin_percent'] < 0.18
    assert 0.33 < round(mc_sims_results['med_drawdown_percent'], 2) < 0.37
    assert 1.80 < mc_sims_results['med_profit_percent'] < 2.00
    assert mc_sims_results['prob_profit_is_positive'] > 0.996

    # print(mc_sims_results)
