import  datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

file_name = "./data/{}.pkl"
possible_prices_file_name = "./data/{}_possible.pkl"
# currency = ["BTC","ETH","XRP","BCH","EOS","LTC","XLM","ADA","MIOTA","TRX","USDT","NEO","DASH","XMR","BNB","XEM"]
currency = ["MIOTA"]
index_future = pd.date_range(start=datetime.date.today(), end='2021-12-30')
index_future.shape
np.random.seed(1234)


data = []
# possible_prices_list = []

def readData():
	for x in currency:
		df = pd.read_pickle(file_name.format(x));
		data.append(df);

readData()

def simulateMonteCarlo(index,data):
	simulated_returns  = np.random.choice(data.returns, size=(len(index_future), 100000))
	sim_returns = pd.DataFrame(data=simulated_returns, index=index_future)
	cum_sim = sim_returns.cumprod(axis=0)
	cum_sim.shape
	future = pd.DataFrame(data=cum_sim, index=index_future)
	future = future * data['close'][data['close'].shape[0]-1]
	# print("Future : ")
	# print(future.head())

	possible_prices = future.iloc[-1, :]
	possible_prices.name = 'Possible price'
	print("{} prices will fall between with 95% probability".format(currency[index]));
	print(possible_prices.quantile(.1), possible_prices.quantile(.95))

	# possible_prices_list.append(possible_prices)
	possible_prices.to_pickle(possible_prices_file_name.format(currency[index]));
	future.iloc[:, :500].plot(legend=False, logy=True, grid=True);
	
	plt.title('{} price Monte Carlo simulations until Dec 31st 2021'.format(currency[index]), size=16)
	plt.ylabel('Price ($)', size=12)
	plt.xlabel('Date', size=12);
	
	plt.show()


for index,x in enumerate(data):
	# print(x['close'][x['close'].shape[0]-1])
	simulateMonteCarlo(index,x);

