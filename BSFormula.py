# web
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
# set starting and end date to import
start = datetime.datetime(2013, 1, 1)
end = datetime.datetime(2017, 2, 27)
# import stock data for 'GOOGL'
df = web.DataReader("GOOGL", 'yahoo', start, end)
#loop over all dates and remove timestamp
#dates=[]
# for x in range(len(df)):
#     newdate = str(df.index[x])
#     newdate = newdate[0:10]
#     dates.append(newdate)
# #  WRONG!  use dataframe map!!!
df['dates'] = df.index.map(lambda x: str(x)[:10])
style.use('fivethirtyeight')
df['High'].plot()
plt.show()
print(df)
