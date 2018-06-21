from cryptory import Cryptory
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import numpy as np

my_cryptory = Cryptory(from_date="2017-01-01")

def plotGraph(metals_df) :
	# metals_df = my_cryptory.get_metal_prices().dropna().merge(
	#  my_cryptory.extract_coinmarketcap(coin)[['date', 'close']], on='date', how='inner')

	for col in metals_df.columns:
	    if col != 'date':
	        metals_df[col] = metals_df[col]/metals_df[col][-1:].values

	fig, ax1 = plt.subplots(1, 1, figsize=(100, 10))

	ax1.set_xticks([datetime.date(j,i,1) for i in range(1,13,2) for j in range(2017, 2019)])
	ax1.set_xticklabels([datetime.date(j,i,1).strftime('%b %d %Y') 
	                     for i in range(1,13,2) for j in range(2017, 2019)])
	for col, col_label, color in zip(['Bitcoin','Ripple','Litecoin','Dash','Monero', 'gold_pm', 'silver', 'platinum_pm', 'palladium_pm'],
	                          ['Bitcoin','Ripple','Litecoin','Dash','Monero', 'Gold', 'Silver', 'Platinum', 'Palladium'],
	                          ['#FF9900', '#FFD700', '#FAFAD1', '#AB1249', '#CEA111','#C0C0C0', '#d23ce8', '#FFFF11','#A12312']):
	    ax1.plot(metals_df['date'].astype(datetime.datetime), 
	             metals_df[col], label=col_label, color=color)
	ax1.set_yscale('log')
	ax1.set_ylim([0.7, 24])
	ax1.legend(bbox_to_anchor=(0.1, 1), loc=2, borderaxespad=0., ncol=2, prop={'size': 14})
	ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: (
	            '{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))
	ax1.set_ylabel('Price (Normalised to Jan 2017)')
	plt.show()


metals_df = my_cryptory.get_metal_prices().dropna()

for x in ['Bitcoin','Ripple','Litecoin','Dash','Monero'] :
	print(x)
	bitcoin = my_cryptory.extract_coinmarketcap(x)[['date', 'close']]
	bitcoin[x] = bitcoin['close']
	bitcoin = bitcoin.drop(['close'],axis=1)
	metals_df = metals_df.merge(bitcoin, on='date',how='inner');
	print(metals_df);

plotGraph(metals_df)


 

# metals_df = my_cryptory.get_metal_prices().dropna().merge(
# 	 my_cryptory.extract_coinmarketcap('bitcoin')[['date', 'close']], on='date', how='inner')
	 
# metal_df=metals_df.merge(my_cryptory.extract_coinmarketcap('ripple')[['date', 'close']], on='date', how='inner')
# print(metals_df)