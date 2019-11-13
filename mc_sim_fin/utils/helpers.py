from pandas import Series, DataFrame
import numpy as np
from typing import Tuple, Dict
import pandas as pd


def get_duration_in_years(date_results: Series) -> float:
    return (date_results.max() - date_results.min()).days/365


def get_nb_trades(date_results: Series) -> int:
    return date_results.count()


def get_avg_trades_per_year(nb_trades_result: int, nb_years_result: float) -> float:
    return nb_trades_result/nb_years_result


def get_nb_trades_for_sample(avg_trades_per_year_result: float,
                             sim_years_duration: float) -> int:
    return round(avg_trades_per_year_result * sim_years_duration)


def get_randomized_trade_results(profit_results: Series,
                                 nb_sim_trade: int) -> Series:
    return profit_results.sample(n=int(nb_sim_trade),
                                 random_state=np.random.RandomState(),
                                 replace=True)


def get_abs_max_drawdown(profit_results: Series) -> float:
    max_drawdown_df = DataFrame()
    max_drawdown_df['cumulative'] = profit_results.cumsum()
    max_drawdown_df['high_value'] = max_drawdown_df['cumulative'].cummax()
    max_drawdown_df['drawdown'] = max_drawdown_df['cumulative'] - max_drawdown_df['high_value']

    return abs(max_drawdown_df['drawdown'].min())


def get_profit(profit_results: Series) -> float:
    return profit_results.sum()


def is_iteration_ruin(profit_results: list, start_capital_amount: float, capital_consider_ruin_amount: float) -> bool:
    max_loss_to_be_ruin = - (start_capital_amount - capital_consider_ruin_amount)
    if Series(profit_results).cumsum().min() < max_loss_to_be_ruin:
        return True
    return False


def get_sim_ruin_probability_percent(sims_is_ruin: list) -> float:
    nb_times_sim_ruin = sims_is_ruin.count(True)
    return nb_times_sim_ruin/len(sims_is_ruin)


def get_sim_median_drawdown_percent(abs_sim_drawdowns_amount: list, start_capital_amount: float) -> float:
    if min(abs_sim_drawdowns_amount) < 0:
        raise ValueError('drawdown_abs_amount must be positive')
    return np.median(abs_sim_drawdowns_amount)/start_capital_amount


def get_sim_median_return_percent(sim_returns_amount: list, start_capital_amount: float) -> float:
    return np.median(sim_returns_amount)/start_capital_amount


def is_iteration_returns_positive(sim_profit_results: Series) -> bool:
    if sim_profit_results.sum() > 0:
        return True
    return False


def get_sim_return_positive_percent(sim_returns_positive: list) -> float:
    nb_sim_positive_returns = sim_returns_positive.count(True)
    return nb_sim_positive_returns/len(sim_returns_positive)


def extract_date_profit_columns(results: DataFrame) -> Tuple[Series, Series]:

    if pd.api.types.is_datetime64_any_dtype(results.iloc[:, 0].dtypes):
        date_results = results.iloc[:, 0]
    else:
        raise TypeError('the first column of the dataframe that represents the date must be a date format')

    if pd.api.types.is_numeric_dtype(results.iloc[:, 1]):
        profit_results = results.iloc[:, 1]
    else:
        raise TypeError('the second column of the dataframe that represents the profit must be a float format')

    return date_results, profit_results


def extract_extra_params(kwargs: Dict) -> Tuple[float, int]:

    expected_args = ['sim_years_duration', 'nb_iterations']

    for key in kwargs:
        if key not in expected_args:
            raise ValueError('the kwargs key {} is not expected only {} allowed'.format(key, expected_args))

    sim_years_duration = kwargs.get('sim_years_duration', 1)
    nb_iterations = kwargs.get('nb_iterations', 10000)

    return sim_years_duration, nb_iterations


def comp_nb_trades_for_sample(date_results: Series, sim_years_duration: int) -> int:
    nb_trades_result = get_nb_trades(date_results)
    nb_years_result = get_duration_in_years(date_results)
    avg_trades_per_year_result = get_avg_trades_per_year(nb_trades_result, nb_years_result)

    return get_nb_trades_for_sample(avg_trades_per_year_result, sim_years_duration)
