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
buyCounter = 4
purchaseLimit = 50.0
maxpurchases =  8
jump = 5.0
total = 0.0
frequency = 40 #seconds
sellCounterInit = 3600/120 #one hour fall
purchases = [0.00599592277251469, 0.00599592277251469, 0.005998080614203455, 0.00599880023995201, 0.0060291812371879895, 0.0060291812371879895, 0.006028454304316373, 0.006019744762822056]


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
	global total, purchaseLimit, BTC, USDT, jump, frequency, purchases, buyCounter
	print "Purchases: ", purchases

	market = getMarketSummary(mktcode)
	current = market['Last']
	if haveOpenOrders(mktcode):
		print "Open Orders, passing for now"
		pass
	else:
		if (getBalance(USDT) > purchaseLimit*(1+0.0025)) and len(purchases)<maxpurchases:
			print "have USDT balance for a purchase of ", purchaseLimit
			if (base <  0) or (current < base):
				buyCounter = 4
				base = current
				print "base price ", base
			elif current < (base + jump):
				pass
			elif current >= (base + jump) and buyCounter == 0:
				print "BTC is ", jump," USDT up, buying it at ",current
				purchaseQuantity = purchaseLimit/current
				if buy(mktcode, purchaseQuantity, current):
					purchases.append(purchaseQuantity)
					buyCounter = 4

			buyCounter -= 1

		if len(purchases) > 0:	
			if current >= maximum:
					maximum = current
			else:		
				notsold = []
				for quantity in purchases:
					purchase = purchaseLimit/quantity
					print "Prices- current: ", current, ", purchase: ", purchase
					sufficientDown = ((maximum - current) >= jump)		#((maximum - current)/maximum > 0.01)#True
					profit = (current*quantity - purchaseLimit - current*quantity*0.0025 - purchaseLimit*0.0025)
					if (profit > 0 and sufficientDown and sell(mktcode, quantity, current)): #current < (purchase+5.0) or (sellcounter == 0):
						total += profit
						print current, purchase, " profit/loss: "+str(profit)+" total:" + str(total)
						buyCounter = 4
					else:	
						notsold.append(quantity)
				purchases = notsold[:]

		

	sch.enter(frequency, 1, TradeMarket, (sch,mktcode,maximum,base, sellcounter))


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(frequency, 1, TradeMarket, (scheduler,mktcode,-1, -1, sellCounterInit))
scheduler.run()

#1198.89999965
#plt.plot(range(len(g)), g)
#plt.ylabel('total profit')
#plt.show()

