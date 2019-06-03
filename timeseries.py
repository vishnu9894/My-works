import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

os.chdir("C:\\Users\\Vishnu\\Desktop\\case study")

dateparse= lambda dates:pd.datetime.strptime(dates,'%Y-%m')
data=pd.read_csv("international-airline-passengers.csv",parse_dates=['Month'],index_col='Month',date_parser=dateparse)

data.head()

data.index

plt.plot(data)

from statsmodels.tsa.stattools import adfuller

moving_avg=data.rolling(3).mean()

plt.plot(data)
plt.plot(moving_avg,color="orange")

adftest=adfuller(data["passenger"],autolag="AIC")

from statsmodels.tsa.seasonal import seasonal_decompose

decomposition=seasonal_decompose(data["passenger"])

trend=decomposition.trend

seasonal=decomposition.seasonal

residual=decomposition.resid

plt.plot(trend,label="trend")

plt.plot(seasonal,label="seasonalty")

plt.plot(residual,label="residuals")

from statsmodels.tsa.arima_model import ARIMA

model=ARIMA(data["passenger"],order=(2,1,2))

results_ar=model.fit()

predictions=pd.Series(results_ar.fittedvalues,copy=True)

plt.plot(data["passenger"])
plt.plot(results_ar.fittedvalues,color="orange")