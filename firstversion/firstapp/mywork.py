import requests

tickerid = {'bitcoin':69045, 'ethereum':4878.26, 'tether':1.32, 'usd-coin':1.17, 'binance-coin':686.31, 'binance-usd':1.15, 'xrp':3.4, 'dogecoin':0.73, 'cardano':3.09, 'polygon':2.92, 'multi-collateral-dai':1.22, 'polkadot':54.98, 'tron':0.23, 'litecoin':410.26, 'shiba-inu':0.000086, 'terra-luna':119.18, 'uniswap':44.92, 'solana':259.96, 'avalanche':144.96, 'unus-sed-leo':144.96, 'wrapped-bitcoin':70643, 'chainlink':52.7, 'monero':52.7, 'cosmos':44.45, 'ethereum-classic':167.09, 'stellar':0.88, 'bitcoin-cash':3785.82, 'crypto-com-coin':0.97 , 'quant':427.42, 'algorand':3.56, 'vechain':0.28, 'internet-computer':700.65, 'near-protocol':20.44, 'filecoin':236.84, 'eos':22.71, 'bitcoin-bep2':489.75, 'paxos-standard':1.13, 'bitcoin-sv':489.75, 'huobi-token':39.66, 'elrond-egld':545.64, 'aave':661.69, 'trueusd':1.62, 'theta':15.72, 'flow':42.4, 'tezos':9.12, 'kucoin-token':28, 'chiliz':0.88, 'zcash':3191.93, 'gemini-dollar':3.3, 'axie-infinity':164.9, 'the-sandbox':8.4, 'hedera-hashgraph':0.57, 'fantom':3.46,'trust-wallet-token':2.72, 'decentraland':5.85, 'pancakeswap':43.96, 'maker':6292.31, 'the-graph':2.84, 'dash':1493.59, 'iota':5.25, 'klaytn':4.34, 'neo':198.38, 'fei-protocol':2.46, 'thorchain':20.87, 'ecash':0.00038, 'mina':9.09, 'nexo':4.07, 'gatetoken':12.94, 'synthetix-network-token':28.53, 'frax-share':42.8, 'lido-dao':4829.57, '1inch':8.65, 'casper':1.33, 'stacks':3.39, 'ftx-token':73, 'curve-dao-token':15.37, 'loopring':3.75, 'nem':1.87, 'zilliqa':0.26, 'basic-attention-token':1.9, 'holo':0.031, 'enjin-coin':4.82,  'helium':52.22, 'compound':911.2, 'defichain':5.61,  'kava':9.19, 'ravencoin':0.29, 'kusama':623.75, 'sushiswap':23.38, 'arweave':90.94, 'rocket-pool':154.73, 'binaryx':224.71, 'terrausd':1.02}



#for max price in last one year
def athprice(ticker):
    url = "https://api.coincap.io/v2/assets/" + ticker + "/history?interval=d1"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    dict = response.json()
    m1 = 0

    for i in dict['data']:
        price = int(float(i['priceUsd']))
        mx = max(m1, price)
        m1 = mx
    return mx


def currprice(ticker):
    url = "https://api.coincap.io/v2/assets"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    dict = response.json()
    for i in dict['data']:
        if i['id'] == ticker:
             price = round(float((i['priceUsd'])),2)
             return price


def relativeChange(ticker):
    initial = tickerid[ticker]
    final = currprice(ticker)
    change= (final-initial)/initial
    #for every 1000rs invested
    finalamount = 1000 +(change*1000)
    return finalamount
#database updation



#print(int(relativeChange('solana')))


for i in tickerid:
    print(i,'all time high price is',tickerid[i],'and current price is',currprice(i))

# for i in tickerid:
#     print('Current price of',i, 'is',currprice(i),'$')

# for i in tickerid:
#     print('Current price of' , i, 'is',currprice(i))

#print(athprice('bitcoin'))
