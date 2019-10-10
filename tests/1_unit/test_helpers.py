import mc_sim_fin.utils.helpers as helpers
from pandas import Series, DataFrame
from datetime import datetime
import numpy as np
import pytest


def test_a_backtest_of_365_days_is_the_same_at_1_year():
    date_results = Series([datetime(2019, 1, 1), datetime(2020, 1, 1)])
    assert helpers.get_duration_in_years(date_results) == 1


def test_a_backtest_with_two_elements_should_be_two_trades():
    profit_amounts = Series([-100, 100])
    assert helpers.get_nb_trades(profit_amounts) == 2


def test_when_my_bot_make_100_trades_in_2_years_he_make_an_average_of_50_trades_per_year():
    assert helpers.get_avg_trades_per_year(100, 2) == 50


def test_when_my_bot_make_on_average_100_trade_per_year_and_i_want_to_simulate_3_years_i_need_300_trades_for_my_simulation():
    assert helpers.get_nb_trades_for_sample(100, 3) == 300


def test_backtest_result_when_simulated_should_be_shuffle():
    nb_trades_for_sample = 100
    profit_results = Series(np.linspace(-1000, 1000, 100))
    result_sim1_amounts = helpers.get_randomized_trade_results(profit_results, nb_trades_for_sample)
    assert profit_results.equals(result_sim1_amounts) is False


def test__4_trades_that_loose_two_times_100_dollar_sould_have_an_absolue_drowdown_of_200_dollar():
    profit_results = Series([-100, 100, -100, -100])
    assert helpers.get_abs_max_drawdown(profit_results) == 200


def test_my_capital_is_4000_i_consider_ruin_at_3500_dollar_the_simulation_loss_700_dollar_so_i_am_ruin():
    assert helpers.is_iteration_ruin([300, -1000], 4000, 3500) is True


def test_during_4_simulations_i_am_ruin_during_1_so_i_get_a_probability_of_25_pecent_to_get_ruin():
    assert helpers.get_sim_ruin_probability_percent([False, False, True, False]) == 0.25


def test_i_make_5_simulations_the_absolute_median_drawdown_is_200_and_my_capital_is_4000_the_median_drawdown_percent_should_be_5_percent():
    assert helpers.get_sim_median_drawdown_percent([1000, 700, 200, 100, 50], 4000) == 0.05


def test_sims_median_drawdown_not_allow_negative_drawdowns():
    with pytest.raises(ValueError):
        helpers.get_sim_median_drawdown_percent([-1000], 4000)


def test_i_make_3_simulations_median_return_is_200_my_start_capital_is_1000_so_i_win_20_percent():
    assert helpers.get_sim_median_return_percent([100, 200, 300], 1000) == 0.20


def test_i_make_simulation_and_the_result_is_1000_dollar_so_my_profit_is_positive():
    assert helpers.is_iteration_returns_positive(Series([-1000, 2000])) is True


def test_i_make_4_simulations_3_gives_me_positive_results_so_i_have_75_percent_probability_to_be_positive():
    assert helpers.get_sim_return_positive_percent([True, False, True, True]) == 0.75


def test_a_two_column_dataframe_with_date_in_first_column_and_float_in_second_should_return_tuple():
    date_results = [datetime(2018, 1, 1), datetime(2018, 12, 31)]
    profit_results = [-100.1, 100]
    df = DataFrame({'date': date_results, 'profit': profit_results})

    date_results_series, profit_results_series = helpers.extract_date_profit_columns(df)
    assert date_results_series.iloc[0] == datetime(2018, 1, 1)
    assert profit_results_series.iloc[0] == -100.1


def test_a_two_column_dataframe_with_float_in_first_column_should_raise_error():
    profit_results = [-100.1, 100]
    date_results = [datetime(2018, 1, 1), datetime(2018, 12, 31)]
    df = DataFrame({'profit': profit_results, 'date': date_results})

    with pytest.raises(TypeError):
        helpers.extract_date_profit_columns(df)


def test_a_two_column_dataframe_with_date_in_second_column_should_raise_error():
    date_results = [datetime(2018, 1, 1), datetime(2018, 12, 31)]
    profit_results = [datetime(2018, 1, 1), datetime(2018, 12, 31)]
    df = DataFrame({'date': date_results, 'profit': profit_results})

    with pytest.raises(TypeError):
        helpers.extract_date_profit_columns(df)


def test_provide_1_year_simulation_10000_simulations_should_return_variable_with_good_infos():
    sim_years_duration, nb_iterations = helpers.extract_extra_params({'sim_years_duration': 1, 'nb_iterations': 10000})
    assert sim_years_duration == 1
    assert nb_iterations == 10000


def test_provide_an_extra_param_key_with_spelling_error_that_doesnt_exist():
    with pytest.raises(ValueError):
        helpers.extract_extra_params({'sim_years_durtion': 1, 'nb_iterations': 10000})
