# Stock history data analysis for position/swing trading
This algorithm analyzes stock history of a given company and investigate various buy/sell triggers.

## buy triggers
A common buy trigger for position and swing traders is to purchase upon the stock price rising above an n-day average.

## sell triggers
Common safeguard paramaters include setting a loss threshold as a percent diffrence from the stocks maximum value during your possession. Selling occurs upon falling below this percent diffrence threshold or if for a given day we drop below the rolling n-day average.

## adjust 
Supply any n-day average duration as your buy trigger, a percent diffrence threshold for selling, and any publicly available company stock history .csv. [Yahoo finance](https://finance.yahoo.com/lookup/) is a great refrence.

## position/swing mindset modeling
This modeling is done considering just the open and close position of a given stock. Unless you are daytrading and able to moniter and make trades during market hours, this modeling may be insightful. Keeping the longer term investment in mind, most position/swing traders check and adjust their positions before and after working hours/market hours and largley just hedge against the opens and closes. 