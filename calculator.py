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

symbols = []
comp_interest = []
apys = []
for i in list_interests:
    symbols.append(i['SYMBOL'][0])
    comp_interest.append(i['COMP'].mean())
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

    x = collateral * time/365 * (apys[market]/100 + comp_interest[market]/100)
    y = (x/collateral*100)
    print('You can expect to see an ROI of {:.2f} or ${:.2f} USD'.format(y,x))

while(1):
    loop()