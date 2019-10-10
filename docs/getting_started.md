# How to install ?

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install montecarlo simulation finance.

```bash
pip install mc-sim-fin
```

# How to use ?

```python

from mc_sim_fin.mc import mc_analysis

#extract the date and the profit from your backtest results
backtest_for_mc_sim = backtest_results[['date','profit']]

"""
provide the equity you start with and the equity you consider as ruin
(it will simulate 1 year of trading with 10 000 iterations)
"""

start_equity = 5000
ruin_equity = 4000

mc_sims_results = mc_analysis(backtest_for_mc_sim,start_equity,ruin_equity)


print(mc_sims_results)

# print output
{
'risk_of_ruin_percent': 0.156,
'med_max_drawdown_percent': 0.36,
'med_profit_percent': 1.83,
'prob_profit_is_positive': 0.9979
}

```

You need to simulate more than 1 year and more/less iterations ? Go to the [API](api.md) doc page
