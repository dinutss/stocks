# API to get basic information about stocks

### This project provides the following API:

1) ```.../info?stock_symbol=<stock_symbol>``` — get information about company.
   
#### Example: .../info?stock_symbol=AAPL```

2) ```.../history?stock_symbol=<stock_symbol>``` — get all historical market data
   
#### Example: .../history?stock_symbol=AAPL

3) ```.../history_interval?stock_symbol=<stock_symbol>&start=<YYY-MM-DD>&to=<YYY-MM-DD>``` — get historical market data from _\<start\>_
   date to _\<end\>_ date
   
#### Example: .../history_interval?stock_symbol=AAPL&start=2020-01-01&end=2020-01-02
   
4)  ```.../chart?stock_symbol=<stock_symbol>&type=<Open/Close/High/Low>``` — get chart of entire historical market data.
    This call returns just a link to the chart
    
#### Example: .../chart?stock_symbol=AAPL&type=Close

