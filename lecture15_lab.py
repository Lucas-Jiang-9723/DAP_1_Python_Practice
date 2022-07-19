# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#prices of Tesla (TSLA) from January 1st 2019 to December 1st 2021.

#Hint: https://www.alphavantage.co/support/#api-key

# 2. Create a new column that holds the rolling 3 month average.

# 3. Create a new dataframe from the base data from part 1 that resamples
# the data to quarterly, using the mean value.

# 4. Create a figure showing the time series for the monthly level and
# the monthly rolling average together.


#%%
import requests
import os
import datetime
import pandas_datareader.data as web
import pandas as pd
#%%
start_date = datetime.datetime(2019, 1, 1)
end_date = datetime.datetime(2021, 12, 1)
key = " OUBOXUTNEDTHI1E6"
tsla = web.DataReader("TSLA", "av-monthly",
                      start=start_date, end=end_date,
                      api_key=key)
tsla.index = pd.to_datetime(tsla.index)
tsla["close_3ma"] = tsla["close"].rolling(3).mean()

#%%
