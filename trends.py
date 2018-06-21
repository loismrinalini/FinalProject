from cryptory import Cryptory
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.pyplot as plt
import datetime


my_cryptory = Cryptory(from_date="2017-01-01")

# btc_google = my_cryptory.get_google_trends(kw_list=['bitcoin']).merge(
# my_cryptory.extract_coinmarketcap('bitcoin')[['date','close']], on='date', how='inner')

# eth_google = my_cryptory.get_google_trends(kw_list=['ethereum']).merge(
# my_cryptory.extract_coinmarketcap('ethereum')[['date','close']], on='date', how='inner')

ltc_google = my_cryptory.get_google_trends(kw_list=['litecoin']).merge(
my_cryptory.extract_coinmarketcap('litecoin')[['date','close']], on='date', how='inner')

iota_google = my_cryptory.get_google_trends(kw_list=['iota']).merge(
my_cryptory.extract_coinmarketcap('iota')[['date','close']], on='date', how='inner')

# ripple_google = my_cryptory.get_google_trends(kw_list=['ripple']).merge(
# my_cryptory.extract_coinmarketcap('ripple')[['date','close']], on='date', how='inner')

doge_google = my_cryptory.get_google_trends(kw_list=['Dogecoin']).merge(
my_cryptory.extract_coinmarketcap('Dogecoin')[['date','close']], on='date', how='inner')

for df,search_term in zip([doge_google, ltc_google, iota_google], 
                          ['Dogecoin', 'litecoin', 'iota']):
    df[[search_term,'close']] = (
        df[[search_term, 'close']]-df[[search_term, 'close']].min())/(
        df[[search_term, 'close']].max()-df[[search_term, 'close']].min())


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9, 6))

for ax in [ax1, ax2, ax3]:
    ax.set_xticks([datetime.date(j,i,1) for i in range(1,13,2) for j in range(2017,2019)])

ax1.set_xticklabels([])
ax2.set_xticklabels([])
ax3.set_xticklabels([datetime.date(j,i,1).strftime('%b %d %Y') for i in range(1,13,2) for j in range(2017,2019)])
for ax,df,search_term, coin, pcol, gcol in zip([ax1, ax2, ax3],[doge_google, ltc_google, iota_google], 
                                               ['Dogecoin', 'litecoin', 'iota'],
                                               ['Dogecoin', 'litecoin', 'iota'], 
                                               ['#FF9900', '#696969', '#00FFFF'],
                                               ['#4885ed', '#4885ed', '#4885ed']):
    ax.plot(df['date'].astype(datetime.datetime),
             df['close'], label=coin, color=pcol)
    ax.plot(df['date'].astype(datetime.datetime),
             df[search_term], label="{} (google search)".format(search_term), color=gcol)
    ax.legend(bbox_to_anchor=(0.1, 1), loc=2, borderaxespad=0., ncol=2, prop={'size': 14})
    ax.text(x=mdates.date2num(datetime.date(2017, 2, 13)), y=0.5, fontsize=13,
         s='Pearson: {}\nSpearman: {}'.format(
        round(df['close'].corr(df[search_term],method='pearson'),3), 
        round(df['close'].corr(df[search_term],method='spearman'),3)))
fig.text(0.005, 0.5, 'Min-Max Normalisation Value', va='center', rotation='vertical',fontsize=12)
plt.tight_layout()
plt.show()