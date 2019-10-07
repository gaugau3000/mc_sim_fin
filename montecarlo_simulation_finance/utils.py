from pandas import Series, DataFrame
import numpy as np


def get_duration_in_years(result_dates: Series) -> float:
    return (result_dates.max() - result_dates.min()).days/365


def get_nb_trades(result_dates: Series) -> int:
    return result_dates.count()


def get_avg_trades_per_year(nb_trades_result: int, nb_years_result: float) -> float:
    return nb_trades_result/nb_years_result


def get_nb_trades_for_sample(avg_trades_per_year_result: float,
                             sim_years_duration: float) -> int:
    return round(avg_trades_per_year_result * sim_years_duration)


def get_randomized_trade_results(result_amounts: Series,
                                 nb_sim_trade: int) -> Series:
    return result_amounts.sample(n=int(nb_sim_trade),
                                 random_state=np.random.RandomState(),
                                 replace=True)


def get_abs_max_drawdown(result_amounts: Series) -> float:
    max_drawdown_df = DataFrame()
    max_drawdown_df['cumulative'] = result_amounts.cumsum()
    max_drawdown_df['high_value'] = max_drawdown_df['cumulative'].cummax()
    max_drawdown_df['drawdown'] = max_drawdown_df['cumulative'] - max_drawdown_df['high_value']

    return abs(max_drawdown_df['drawdown'].min())


def get_profit(result_amounts: Series) -> float:
    return result_amounts.sum()


def is_sim_ruin(result_amounts: list, start_capital_amount: float, capital_consider_ruin_amount: float) -> bool:
    max_loss_to_be_ruin = - (start_capital_amount - capital_consider_ruin_amount)
    if Series(result_amounts).cumsum().min() < max_loss_to_be_ruin:
        return True
    return False


def get_sims_ruin_probability_percent(sims_is_ruin: list) -> float:
    nb_times_sim_ruin = sims_is_ruin.count(True)
    return nb_times_sim_ruin/len(sims_is_ruin)


def get_sims_median_drawdown_percent(abs_sim_drawdowns_amount: list, start_capital_amount: float) -> float:
    if min(abs_sim_drawdowns_amount) < 0:
        raise ValueError('drawdown_abs_amount must be positive')
    return np.median(abs_sim_drawdowns_amount)/start_capital_amount


def get_sims_median_return_percent(sim_returns_amount: list, start_capital_amount: float) -> float:
    return np.median(sim_returns_amount)/start_capital_amount


def is_sim_returns_positive(sim_result_amounts: Series) -> bool:
    if sim_result_amounts.sum() > 0:
        return True
    return False


def get_sims_return_positive_percent(sim_returns_positive: list) -> float:
    nb_sim_positive_returns = sim_returns_positive.count(True)
    return nb_sim_positive_returns/len(sim_returns_positive)
