from yahoofinancials import YahooFinancials
import pandas as pd
import numpy as np
import pdb
import time


CSV_PATH = './data/asx200Tickers.csv'
OUTPUT_PATH = './data/stockData.csv'

def tickers_from_csv(csvPath, asxStocks=True, nStocks=-1):
	"""load a list of tickers from a csv file, with the column named
	tickers"""

	tickerDataFrame = pd.read_csv(csvPath)
	tickerSeries = tickerDataFrame['ticker'][0:nStocks]
	
	#get the list of tickers from the column named ticker
	#create ASX stocks by appending .AX to the stock name
	if asxStocks:
		for i in range(len(tickerSeries)):
			tickerSeries[i] = tickerSeries[i] + '.AX'

	print('Loaded in tickers series -->\n ', tickerSeries)

	return tickerSeries


if __name__ == '__main__':

	#load ticker series
	#here we use the ASX 200 largest companies by market capitalisation
	tickerSeries = tickers_from_csv(CSV_PATH, nStocks=5)

	#create the YahooFinancials connection object
	stocks = YahooFinancials(tickerSeries)

	#Pull the data and time it
	startTime = time.time()
	data = stocks.get_summary_data()
	timeTaken = time.time()-startTime
	print('Download took {t} seconds'.format(t=timeTaken))

	stockDataFrame = pd.DataFrame(data)
	stockDataFrame.to_csv(OUTPUT_PATH)