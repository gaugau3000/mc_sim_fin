[![Build Status](https://travis-ci.org/gaugau3000/mc_sim_fin.svg?branch=master)](https://travis-ci.com/gaugau3000/mc_sim_fin)
[![codecov](https://codecov.io/gh/gaugau3000/mc_sim_fin/branch/master/graph/badge.svg)](https://codecov.io/gh/gaugau3000/mc_sim_fin)
[![PyPI](https://img.shields.io/pypi/v/mc-sim-fin)](https://pypi.org/project/mc-sim-fin/)

# Montecarlo simulations/analysis for finance (equity simulator)

An inspiration of the book [BUILDING WINNING ALGORITHMIC TRADING SYSTEMS](https://www.amazon.com/Building-Winning-Algorithmic-Trading-Systems/dp/1118778987) of 'Kevin J. Davey' (chapter 7 detailed analysis)

As an algorithmic trader I want to know what's my risk of ruin on 1 year of trading so that I can manage the risk.  
As an algorithmic trader I want to know the median drawdown on 1 year of trading so that I can expect as reference drawdown from my bot.  
As an algorithmic trader I want to know the median return on 1 year of trading so that I can expect as reference gain from my bot.  
As an algorithmic trader I want to know the probability that the bot make profit during the first year so that I can be patient.  

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install montecarlo simulation finance.

```bash
pip install mc-sim-fin
```

## Usage

You have 5000 dollar for trading, you stop trading if you capital go below 4000. Your bot make one trade per day and alternate a win trade of 200 then a lose trade of 150 during one year. What's happened if the trades came in an other order ?

```python
import pandas as pd
import numpy as np
from mc_sim_fin.mc import mc_analysis


start_equity = 5000
consider_ruin_equity = 4000

result_dates = pd.date_range(start='1/1/2017', end='31/12/2017').tolist()
result_amounts = np.resize([200, -150], 365)

df = pd.DataFrame({'result_dates': result_dates, 'result_amounts': result_amounts})

mc_sims_results = mc_analysis(df['result_dates'], df['result_amounts'], start_equity, consider_ruin_equity)


print(mc_sims_results)

# print output
{
'risk_of_ruin_percent': 0.156,
'med_drawdown_percent': 0.36,
'med_profit_percent': 1.83,
'prob_profit_is_positive': 0.9979
}

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please cover your code by tests and run : pytest --flake8

You can build your dev image thanks to the Dockerfile.dev

## License
[MIT](https://choosealicense.com/licenses/mit/)
