#calculator for loan maturity

#imports
from datetime import datetime
import utils

#####
interests = utils.loaddata(utils.interests)
txs = utils.loaddata(utils.txs)
list_txs = utils.group(txs)
list_interests = utils.group(interests)
del interests,txs

list_txs = utils.reindex(list_txs)
list_interests = utils.reindex(list_interests)
list_txs[7] = list_txs[7].append(list_txs[8])
del list_txs[8]

list_txs.insert(6,list_txs[3])
del list_txs[3]

avgcomps = utils.cOMPS(list_interests,list_txs)

symbols = []
for i in list_interests:
    symbols.append(i['SYMBOL'][0])
    # print(i['SYMBOL'][0])
    comp_interest = []
for i in avgcomps:
    # print('31 Day Average COMP for different markets {:.4f}'.format(utils.np.mean(i)))
    comp_interest.append(utils.np.mean(i))
apys = []
for i in list_interests:
    # print('31 Day Average APY for different markets {:.4f}'.format(i['APY'].mean()))
    apys.append(i['APY'].mean())
####

def loop():
    #get inputs
    currentdate = datetime.now()
    print('\n*********COMPOUND ROI Calculator*********'.format(currentdate.strftime('%b %d, %Y')))
    collateral = float(input('Enter your initial collateral amount (in USD):'))

    print('=========================')
    for ind,val in enumerate(symbols):
        print('[{}]:{}'.format(ind,val))
    market = int(input('Choose your market by entering the associated number:'))
    time = int(input('Enter the amount of days you would like to leave your supply:'))

    x = collateral * apys[market] * time/365 + time * comp_interest[market]
    print('You can expect to see an ROI of {:.2f}'.format(x/collateral*100))

while(1):
    loop()