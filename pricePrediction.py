import  datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats  import gaussian_kde

possible_prices = []
possible_prices_file_name = "./data/{}_possible.pkl"
currency = ["BTC","ETH","XRP","BCH","EOS","LTC","XLM","ADA","MIOTA","TRX","USDT","NEO","DASH","XMR","BNB","XEM"]
# currency = ["ETH","XRP"]

def readData():
	for x in currency:
		df = pd.read_pickle(possible_prices_file_name.format(x));
		possible_prices.append(df);

def plotDistribution(index,data) : 
	y, x, _ = plt.hist(np.log(data), bins=200);
	xticks = plt.xticks()
	ticks = np.linspace(min(np.log(data)), max(np.log(data)), 10)
	plt.xticks(ticks, [str(int(np.exp(tick))) for tick in ticks]);

	plt.xlabel('Price ($)')
	plt.ylabel('Number of random walks')
	plt.title('Distribution of {} simulated prices by Dec 31st 2021'.format(currency[index]), size=16);
	plt.show()

readData()


def plotDensityDistribution(index,data,step):
	fig, ax = plt.subplots()
	
	ax.hist(np.log(data), bins=150, density=True, label='Final simulated price');
	xticks = plt.xticks()
	hand_ticks = step
	
	ax.set_xticks([],[])
	# ax.set_xticklabels([],[])

	kde = gaussian_kde(np.log(data))
	
	x = np.linspace(max(np.log(data)), min(np.log(data)))
	
	ax.plot(x, kde.pdf(x), linewidth=3, c='orange', alpha=1, label='KDE density function')

	# Plot vertical line at the most likely price
	most_likely_price = np.exp(x[np.argmax(kde.pdf(x))])
	
	# most_likely_price = possible_prices.quantile(0.5)
	# print("most_like_price : ")
	# print(most_likely_price)
	ax.vlines(np.log(most_likely_price), 0, kde.pdf(np.log(most_likely_price)), color='w')

	# Draw annotation
	ax.annotate('Most likely price: ${}'.format(int(round(most_likely_price))), 
            xy=(np.log(most_likely_price), kde.pdf(np.log(most_likely_price))), 
            xytext=(5, 0.02),
            arrowprops=dict(facecolor='black', shrink=0.0),
            size=14)

	plt.legend()

	plt.xlabel('Price ($) (log scale)', size=12)
	plt.ylabel('Density', size=12)
	plt.title('Distribution of {} simulated prices by Dec 31st 2018'.format(currency[index]), size=16)


	plt.show()

# for index,data in enumerate(possible_prices):
# 	plotDistribution(index,data);

for index,data in enumerate(possible_prices):
	
	# step = int((data.max() - data.min())/10)
	# step = 1 if step < 1 else step
	# tick =list(range(int(data.min()),int(data.max())+1,step))
	
	# plotDensityDistribution(index,data,tick)
	
	possible_prices[index] = pd.DataFrame(possible_prices[index])
	# print(np.percentile(possible_prices[index],.1),np.percentile(possible_prices[index],.95),np.percentile(possible_prices[index],.5))
	# print(pd.Series(possible_prices[index]).quantile([.5]))


