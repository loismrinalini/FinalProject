import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from cryptocmd import CmcScraper

# initialise scraper
fileName = "./data/{}.pkl"
currency = ["BTC","ETH","XRP","BCH","EOS","LTC","XLM","ADA","TRX","NEO","DASH","XMR","BTC"]
# currency = ["ETH","XRP","BCH","EOS"]

extractedData = []

def plotGraph(df):
	for index,x in enumerate(df): 
		plt.plot(x['Date'],x['close'],label=currency[index])

	plt.title("CLOSE")
	plt.ylabel('close ($)')
	plt.xlabel('Date')
	plt.legend()
	plt.show()

for x in currency:
	scraper = CmcScraper(x, '1-1-2014', '18-6-2018')
	df = scraper.get_dataframe()
	df["Close**"].replace(0,np.nan,inplace=True)
	df["close"] = df["Close**"]
	df['returns'] = (df['close'].pct_change() + 1).fillna(1)
	df = df.loc[:,['Date','close','returns']]
	df = df.dropna()

	# plotGraph(df)
	print(x)
	print(df.head())
	df.to_pickle(fileName.format(x))
	extractedData.append(df)

plotGraph(extractedData)

