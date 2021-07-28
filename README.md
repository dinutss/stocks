# API to get basic information about stocks

!This project is hosted on https://www.pythonanywhere.com/

### This project provides the following API:

1) ```.../info?stock_symbol=<stock_symbol>``` — get information about company.
   
#### Example: https://dinutss.pythonanywhere.com/info?stock_symbol=AAPL```

2) ```.../history?stock_symbol=<stock_symbol>``` — get all historical market data
   
#### Example: https://dinutss.pythonanywhere.com/history?stock_symbol=AAPL

3) ```.../history_interval?stock_symbol=<stock_symbol>&start=<YYY-MM-DD>&to=<YYY-MM-DD>``` — get historical market data from _\<start\>_
   date to _\<end\>_ date
   
#### Example: https://dinutss.pythonanywhere.com/history_interval?stock_symbol=AAPL&start=2020-01-01&end=2020-01-10
   
4)  ```.../chart?stock_symbol=<stock_symbol>&type=<Open/Close/High/Low>``` — get chart of entire historical market data.
    This call returns just a link to the chart
    
#### Example: https://dinutss.pythonanywhere.com/chart?stock_symbol=AAPL&type=Close

