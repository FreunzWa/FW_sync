import pandas as pd
import yfinance as yf
import yahoofinancials
import pdb
from tqdm import tqdm
import numpy as np

#loads in all required tickers
tickers = pd.read_csv('./SP500tickers.csv').values

#create a container that will be used to contain all ticker strings that
#produce bad data when the data is downloaded.
errorList = []

#data time range
startTime = '2018-01-02'
endTime = '2018-7-01'

#create a list of tickers for input into the download function
#reshape the numpy array to a 1D-array
tickerList = list(np.reshape(tickers, (tickers.shape[0],)))

#prepare the tickerstrings for the yf download function
for i in range(len(tickerList)-1):
	tickerList[i] = tickerList[i].replace(' ', '')
	print(tickerList[i] ,)

#download all ticker entries into a pandas dataframe
stockChartData = yf.download(
	tickerList, 
	threads=True, 
	group_by='ticker',
	period='2y'
	)

#save the stock pandas dataframe to a csv file.
stockChartData.to_csv('./stockChartData.csv')	

"""
def get_stock_data_by_ticker_list(tickersList):

	#create containers for all required data series, 1 entry per stock.
	closePriceList = []
	volumeList = []

	print('Pulling stock price information ... ')
	for ticker in tqdm(tickers):
		tickerString = ticker[0].replace(' ','')
		stockDataFrame = yf.download(tickerString,
									start=startTime, 
									end=endTime,
									progress=False
									).fillna(method='ffill').fillna(method='bfill')
		#append this tickers' data to each of the containers defined above.
		closePriceList.append(stockDataFrame['Close'].rename(tickerString))
		volumeList.append(stockDataFrame['Volume'].rename(tickerString))	

	return closePriceList, volumeList


closePriceList, volumeList = get_stock_data_by_ticker_list(tickers)


#create the dataframes to save
closePriceDataFrame = pd.concat((closeList for closeList in closePriceList), axis=1)
volumeDataFrame = pd.concat((volumeSeries for volumeSeries in volumeList), axis=1)\

#drop columns with null values.
closePriceDataFrame.dropna(axis=1, inplace=True)
volumeDataFrame.dropna(axis=1, inplace=True)
"""
