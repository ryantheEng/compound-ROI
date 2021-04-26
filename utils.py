#imports
import json
from urllib import request as rq
import pandas as pd
import numpy as np

txs = 'https://api.flipsidecrypto.com/api/v2/queries/1d4aa346-e60f-48e0-aa06-43af88bcbce9/data/latest'
interests = 'https://api.flipsidecrypto.com/api/v2/queries/0f0ebfaa-31ed-486f-9866-19de92de1903/data/latest'

comp_users = 300000

#input url API
#output dataframe
def loaddata(url):
    dataset = rq.urlopen(url)
    dataset = dataset.read()
    dataset = json.loads(dataset)
    return pd.DataFrame(dataset)

def group(dataset:pd.DataFrame):
    gb = dataset.groupby('SYMBOL')
    return [gb.get_group(a) for a in gb.groups]

def reindex(datasets:list):
    for dataset in datasets:
        dataset.reset_index(drop=True,inplace=True)
    return datasets

# def averageCOMP(comp:pd.Series,blocks:pd.Series):
#     avgCOMP = []
#     if len(blocks) < len(comp):
#         if len(comp)-len(blocks) > 1:
#             del comp[0:len(comp)-len(blocks)]
#         else:
#             del comp[0]
#         comp.reset_index(drop=True,inplace=True)
#     elif len(blocks) > len(comp):
#         if len(blocks)-len(comp) > 1:
#             del blocks[0:len(blocks)-len(comp)]
#         else:
#             del blocks[0]
#     blocks.reset_index(drop=True,inplace=True)
#     for index, val in blocks.iteritems():
#         x = comp[index]*val/comp_users #comp * blocks / users
#         if x > 100000000:
#             x = 0
#         else:
#             avgCOMP.append(comp[index]/val)
#     return avgCOMP

# def cOMPS(list_interests,list_txs):
#     i=0
#     tmp = []
#     avgcomp = []
#     while i < len(list_txs):
#         tmp.append(averageCOMP(list_interests[i]['COMP'],list_txs[i]['BLOCKS']))
#         avgcomp.append((tmp))
#         tmp = []
#         i+=1
#     return avgcomp

# def plotone(title:str,series:pd.Series):
#     plt.plot(np.arange(0,len(series),1),series)
#     plt.ylabel('Value (USD)')
#     plt.legend()
#     plt.title(title,pad=20)

# colours = ['lightseagreen','paleturquoise','teal','darkslategray','deepskyblue','lightslategrey']
# def plotter(title:str,datasets:list):
#     fig,ax = plt.subplots()
#     for ind,dataset in enumerate(datasets):
#         plt.plot(np.array(dataset.index),dataset['AVG(FEE_USD)'],color=colours[ind],label=dataset['FUNCTION_NAME'][1])
#         print('Average Fee for '+dataset['FUNCTION_NAME'][1]+':${:.2f} USD'.format(dataset['AVG(FEE_USD)'].mean()))
#     ax.set_xticks([])
#     ax.set_xlabel('Last 90 Days')
#     ax.set_ylabel('Average Fee (USD)')
#     plt.legend()
#     plt.title(title,pad=20)

# interests = loaddata(interests)
# txs = loaddata(txs)
# list_txs = group(txs)
# list_interests = group(interests)
# del interests,txs
# list_txs = reindex(list_txs)
# list_interests = reindex(list_interests)
# list_txs[7] = list_txs[7].append(list_txs[8])
# del list_txs[8]
# list_txs.insert(6,list_txs[3])
# del list_txs[3]
# avgcomps = cOMPS(list_interests,list_txs)