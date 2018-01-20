import crypto_bot
import threading
import sched, time
import json
import matplotlib.pyplot as plt

BTC = 'BTC'
USDT = 'USDT'
mktcode = 'USDT-BTC'
key = ""
secret = ""
api = crypto_bot.bittrex(key, secret)
purchaseLimit = 155.0
jump = 0.01
total = 0.0
frequency = 300 #seconds
lastSellPrice = 100000000
sellCounterInit = 3600/120 #one hour fall
purchases = []

def getMarketSummary(mktcode):	
	global api
	d = api.getmarketsummary(mktcode)[0]
	return d

def buy(market, quantity, rate):	
	global api
	print "Buying : ", market, quantity, rate
	transaction = api.buylimit(market, quantity, rate)
	uuid = ''
	if transaction.has_key('uuid'):
		uuid = transaction['uuid']	
	return (uuid != '') 

def sell(market, quantity, rate):	
	global api
	print "Selling : ", market, quantity, rate
	transaction = api.selllimit(market, quantity, rate)
	uuid = ''
	if transaction.has_key('uuid'):
		uuid = transaction['uuid']	
	return (uuid != '')

def getBalance(currency):
	balance = 0
	result = api.getbalance(currency)
	if result.has_key('Available'):
		balance = result['Available']
	else:
		print "get balance api is failing"
	return balance

def haveBalance(quantity, rate, currency):
	global purchaseLimit
	balance = getBalance(currency)
	if currency == USDT:
		return (balance > (purchaseLimit*(1+0.0025)))
	else:		
		exptdbal = quantity/float(rate)
		return (abs(balance - exptdbal) < 0.00000001)

def haveOpenOrders(market):
	result = api.getopenorders(market)
	return (result != 'INVALID_MARKET' and len(result) > 0)

def TradeMarket(sch, mktcode, maximum, base, sellcounter):
	global total, purchaseLimit, BTC, USDT, jump, frequency,lastSellPrice
	market = getMarketSummary(mktcode)
	current = market['Last']

	if haveOpenOrders(mktcode):
		print "Open Orders, passing for now"
		pass
	else:	
		quantity = getBalance(BTC)
		if quantity > 0.00001:
			purchase = purchaseLimit/quantity
			print "Dealing with ", quantity, " BTC Units"
			print "Prices- current: ", current, ", purchase: ", purchase
			if quantity>0.0:
				if current >= maximum:
					maximum = current
				else:
					sufficientDown = ((maximum - current) > maximum*jump)
					profit = (current*quantity - purchaseLimit - current*quantity*0.0025 - purchaseLimit*0.0025)
					if (profit > 0 and sufficientDown and sell(mktcode, quantity, current)):
						total += profit
						print current, purchase, " profit/loss: "+str(profit)+" total:" + str(total)
						#g.append(total)
						base = -1
						purchase = -1
						lastSellPrice = current
					else:	
						pass
		elif haveBalance(0,1,USDT):
			print "have usdt balance"
			if base < 0:
				base = current
				print "Initializing base price ", base
			elif current < base:	
				base = current
				print "Updating base price ", base
			elif current < (base + base*jump):
				pass
			elif current >= (base + base*jump) and (current < lastSellPrice):
				print "BTC is percent ", jump*100," up, buying it at ",current
				purchaseQuantity = purchaseLimit/current
				if buy(mktcode, purchaseQuantity, current):
					maximum = current
					purchase = current			
		else:
				print "****************** Weird State, please have a look *****************************"			

	sch.enter(frequency, 1, TradeMarket, (sch,mktcode,maximum,base, sellcounter))


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(frequency, 1, TradeMarket, (scheduler,mktcode,-1, -1, sellCounterInit))
scheduler.run()

#1198.89999965
#plt.plot(range(len(g)), g)
#plt.ylabel('total profit')
#plt.show()

