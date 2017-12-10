import crypto_bot
import threading
import sched, time
import json, math
import matplotlib.pyplot as plt

BCC = 'BCC'
USDT = 'USDT'
mktcode = 'USDT-BCC'
key = ""
secret = ""
api = crypto_bot.bittrex(key, secret)
purchaseLimit = 200.0
jump = 0.01
total = 0.0
frequency = 60 #seconds
UUID = None
sellcounter = 0

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
		UUID = uuid 
	return (uuid != '')

def sell(market, quantity, rate):	
	global api
	print "Selling : ", market, quantity, rate
	transaction = api.selllimit(market, quantity, rate)
	uuid = ''
	if transaction.has_key('uuid'):
		uuid = transaction['uuid']
		UUID = uuid 	
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
	if currency == 'USDT':
		return (balance > (purchaseLimit*(1+0.0025)))
	else:		
		exptdbal = quantity/float(rate)
		return (abs(balance - exptdbal) < 0.00000001)

def haveOpenOrders(market):
	result = api.getopenorders(market)
	return (result != 'INVALID_MARKET' and len(result) > 0)

def TradeMarket(sch, mktcode, maximum, base):
	global total, purchaseLimit, BCC, USDT, jump, frequency	, UUID, sellcounter
	market = getMarketSummary(mktcode)
	current = market['Last']

	if haveOpenOrders(mktcode):
		print "Open Order, trying to cancel it"
		api.cancel(UUID)
		UUID = None
	else:
		quantity = getBalance(BCC)
		if quantity > 0.001:
			purchase = purchaseLimit/quantity
			print "Dealing with ", quantity, " BCC Units"
			print "Prices- current: ", current, ", purchase: ", purchase, ", maximum: ", maximum
			if current >= maximum:
				maximum = current
			else:
				sellcounter = sellcounter - 1
				waitsell = (sellcounter == 0)
				sufficientDown = ((maximum - current)/maximum > 5*jump)
				profit = (current*quantity - purchaseLimit - current*quantity*0.0025 - purchaseLimit*0.0025)
				if (profit > 0 and sufficientDown and waitsell and sell(mktcode, quantity, current)): 
					total += profit
					print current, purchase, " profit/loss: "+str(profit)+" total:" + str(total)
					base = current - 0.01*current
				else:	
					pass
		elif haveBalance(0,1,USDT):
			print "have usdt balance"
			if base < 0 or current < base:
				base = current
				print "Updating base price ", base
			elif current < (base + jump*base):
				pass
			elif current >= (base + jump*base):
				print "BCC is 1 percent up, buying it at " + str(current)
				purchaseQuantity = purchaseLimit/current
				if buy(mktcode, purchaseQuantity, current):
					maximum = current
					purchase = current
					sellcounter = math.ceil(180/frequency)
		else:
				print "****************** Weird State, please have a look *****************************"

	sch.enter(frequency, 1, TradeMarket, (sch,mktcode,maximum,base))


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(frequency, 1, TradeMarket, (scheduler,mktcode,-1, -1))
scheduler.run()

