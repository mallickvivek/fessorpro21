
#Dictionary

stock_prices={'amzn':100, 'tsla':200, 'goog':600}

print(stock_prices['tsla'])

print(stock_prices.get('nifty'))

# a='nifty'
# print(a[9])

#read
print(stock_prices['amzn'])
print(stock_prices.get['amzn'])

#update
#stock_prices['amzn']=200
stock_prices.update{'amzn':200}
print(stock_prices)

#create/write
#stock_prices.update({'nifty':800})
stock_prices;['nifty']=800
print(stock_prices)

#delete
#stock_prices.pop('tsla')
del stock_prices['tsla']
print(stock_prices)

