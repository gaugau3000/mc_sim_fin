# Work In Progress - Work In Progress - Work In Progress - Work In Progress - Work In Progress - Work In Progress

# Montecarlo simulations for finance

An inspiration of the book [BUILDING WINNING ALGORITHMIC TRADING SYSTEMS](https://www.amazon.com/Building-Winning-Algorithmic-Trading-Systems/dp/1118778987) of 'Kevin J. Davey' (chapter 7 detailed analysis)


As an algorithmic trader I want to know what's my risk of ruin on 1 year of trading so that I can manage the risk.
As an algorithmic trader I want to know the median drawdown on 1 year of trading so that I can expect as reference drawdown from my bot.
As an algorithmic trader I want to know the median return on 1 year of trading so that I can expect as reference gain from my bot.
As an algorithmic trader I want to know the probability that the bot make profit during the first year so that I can project and be patient :-).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install montecarlo simulation finance.

```bash
pip install mc-sim-fin
```

## Usage



```python
from montecarlo_simulation_finance.montecarlo import mc_sims

start_equity = 5000
consider_ruin_equity = 4000

mc_sims_results = mc_sims(df['result_dates'], df['result_amounts'], start_equity, consider_ruin_equity)


print(mc_sims_results)

# print output
{
'risk_of_ruin_percent': 0.1565,
'med_drawdown_percent': 0.36,
'med_return_percent': 1.9,
'prob_returns_positive': 0.9981
}

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
