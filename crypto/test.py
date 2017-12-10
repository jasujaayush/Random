import crypto_bot
import threading
import sched, time
import json, math
import matplotlib.pyplot as plt

BCC = 'BTC'
USDT = 'USDT'
mktcode = 'USDT-BTC'
key = ""
secret = ""
api = crypto_bot.bittrex(key, secret)
purchaseLimit = 1000.0
total = 0.0
frequency = 150 #seconds
count = 0
base = -1
quantity = 0
price = -1

def getMarketSummary(mktcode):	
	global api
	d = api.getmarketsummary(mktcode)[0]
	return d

def TradeMarket(sch, mktcode, maximum):
	global total, purchaseLimit, BCC, USDT, frequency, count, base, quantity, price
	market = getMarketSummary(mktcode)
	current = market['Last']

	if base < 0:
		base = current
		count += 1
	else:
		if (quantity > 0) and (current - price) > (0.03*price):
			profit = (current*quantity - purchaseLimit - current*quantity*0.0025 - purchaseLimit*0.0025)	
			total += profit
			quantity = 0
			print current, purchase, " profit/loss: "+str(profit)+" total:" + str(total)
		elif (current < (0.975*base)):
			print "Bought at - ", current, " average - ", base
			price = current
			quantity = purchaseLimit/price
		base = current
		count += 1
		if count%10 == 0:
			print count, " base - ", base

	sch.enter(frequency, 1, TradeMarket, (sch,mktcode,maximum))


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(frequency, 1, TradeMarket, (scheduler,mktcode,-1, -1))
scheduler.run()


'''
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
				print "****************** Weird State, please have a look *****************************
'''
