import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

fileName = "./data/{}.pkl"
currency = ["BTC","ETH","XRP","BCH","EOS","LTC","XLM","ADA","MIOTA","TRX","USDT","NEO","DASH","XMR","BNB","XEM"]
# currency = ["ETH","XRP","BCH","EOS"]

data = []

def readData():
	for x in currency:
		df = pd.read_pickle(fileName.format(x));
		data.append(df);

def plotNormalDistribution():
	for index,value in enumerate(data):
		parameters = norm.fit(value.returns - 1)
		x = np.linspace(min(value.returns - 1), max(value.returns - 1), 100)
		fitted_pdf = norm.pdf(x,loc = parameters[0],scale = parameters[1])
		normal_pdf = norm.pdf(x)
		plt.plot(x,fitted_pdf,label="Fitted normal distribution {}".format(currency[index]))
		# plt.plot(x,normal_pdf,"blue",label="Normal dist", linewidth=2)
		plt.hist(value.returns - 1,normed=1,color="b",alpha=.3, bins=200, label="Daily returns {}".format(currency[index])) #alpha, from 0 (transparent) to 1 (opaque)
		plt.title("Returns and normal fitting")
		# insert a legend in the plot (using label)
		plt.legend()	
		plt.show()
	

readData()
plotNormalDistribution()

# print(data);
