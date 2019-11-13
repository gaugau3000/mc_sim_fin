# Montecarlo simulations/analysis for finance (equity simulator)

[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Build Status](https://travis-ci.org/gaugau3000/mc_sim_fin.svg?branch=master)](https://travis-ci.com/gaugau3000/mc_sim_fin)
[![codecov](https://codecov.io/gh/gaugau3000/mc_sim_fin/branch/master/graph/badge.svg)](https://codecov.io/gh/gaugau3000/mc_sim_fin)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/37f78d31316241e4b97126c340975652)](https://www.codacy.com/manual/gaugau3000/mc_sim_fin?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gaugau3000/mc_sim_fin&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/5aeaf6091ec31dd12b60/maintainability)](https://codeclimate.com/github/gaugau3000/mc_sim_fin/maintainability)
[![PyPI](https://img.shields.io/pypi/v/mc-sim-fin)](https://pypi.org/project/mc-sim-fin/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/gaugau3000/mc_sim_fin/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

An inspiration of the book [BUILDING WINNING ALGORITHMIC TRADING SYSTEMS](https://www.amazon.com/Building-Winning-Algorithmic-Trading-Systems/dp/1118778987) of 'Kevin J. Davey' (chapter 7 detailed analysis)

What's happened if your trades happened in an other order and you do that many times to produce statistics ? What are your chances to be ruin ? What's maximum drawdown you may met ?

Giving the trade results to the library and it will help you to manage the risk.

CAUTION : The simulator include assumption that your trades are independent one from the others : it may be the case if your bots make more than one trade at the same time on correlated markets (you can use a durbin watson statistic from [statsmodels library](https://www.statsmodels.org/dev/generated/statsmodels.stats.stattools.durbin_watson.html) to see that)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install montecarlo simulation finance.

```bash
pip install mc-sim-fin
```

## Usage

For the code example below you have 5000 dollar for trading, you stop trading if you capital go below 4000. Your backtest results show that you bot make one trade per day and alternate a win trade of 200 then a lose trade of 150 during the 2017 year.

By default it simulate 1 year of trading with 10000 iterations (look at the documentation to modify this params).

```python
import pandas as pd
import numpy as np
from mc_sim_fin.mc import mc_analysis


date_results = pd.date_range(start='1/1/2017', end='31/12/2017').tolist()
profit_results = np.resize([200, -150], 365)

results = pd.DataFrame({'date_results': date_results, 'profit_results': profit_results})

mc_sims_results = mc_analysis(results, start_equity=5000, ruin_equity=4000)


print(mc_sims_results)

# print output
{
'risk_of_ruin_percent': 0.156,
'med_max_drawdown_percent': 0.36,
'med_profit_percent': 1.83,
'prob_profit_is_positive': 0.9979
}

```

So I have 15.6% changes to be ruin, I can expect 36% max drawdown and 183% profit and I have 99.79% change to win money during the first year.

## Documentation

You need more information about how the simulation work? You would like to contribute ?

Look at the [documentation](https://gaugau3000.github.io/mc_sim_fin/)

## License

[MIT](https://choosealicense.com/licenses/mit/)
