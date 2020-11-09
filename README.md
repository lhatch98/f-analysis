# Stock history data analysis for position/swing trading
This algorithm analyzes stock history of a given company and investigate various buy/sell triggers.

## 📈 buy triggers
A common buy trigger for position and swing traders is to purchase upon the stock price rising above an n-day average.

## 📉 sell triggers
Common safeguard paramaters include setting a loss threshold as a percent difference from the stocks maximum value during your possession. Selling occurs upon falling below this percent difference threshold or if for a given day we drop below the rolling n-day average.

## ⚙️ adjust 
Supply any n-day average duration as your buy trigger, a percent difference threshold for selling, and any publicly available company stock history .csv. I used data from [Yahoo finance](https://finance.yahoo.com/lookup/) and my csv data parser method expects that format so best to use this source.

### cli arguments
Run ```python3 n_year_algo2.py -h``` to see all possible arguments and their details. The ```-f``` flag required and is the file path to your data. The ```-n``` and ```-p``` flags are for the optional running average days and percent difference threshold which default to 40 and 10% respectively. 


## 📊 position/swing mindset modeling
This modeling is done considering just the open and close position of a given stock. If you are daytrading and able to moniter and make trades during market hours, this modeling won't be as useful. Keeping the longer term investment in mind, most position/swing traders check and adjust their positions before and after working hours/market hours and largley just hedge against the opens and closes.

## dependencies
This program uses matplotlib for visualizations. If you don't already have it installed, run
```python3 -m pip install matplotlib```
to install it and its corresponding dependencies.

