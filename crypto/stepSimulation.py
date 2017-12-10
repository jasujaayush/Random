import crypto_bot
import threading
import sched, time
import json
import matplotlib.pyplot as plt
import random

BCC = 'BCC'
USDT = 'USDT'
mktcode = 'USDT-BCC'
key = ""
secret = ""
api = crypto_bot.bittrex(key, secret)
ustdBalance = 210
purchaseLimit = 50
jump = 10
total = 0
frequency = 0.001 #seconds
quantity = 0
purchases = []

data = json.load(open("GetTicks.json"))["result"]
minute = 0
g = []

def getMarketSummary(mktcode):	
	global api,minute
	d = {'Last':data[minute]['H']}
	minute += 1
	return d

def buy(market, quantity, rate):	
	return True

def sell(market, quantity, rate):	
	return True

def haveOpenOrders(market):
	False

def TradeMarket(sch, mktcode, maximum, base, sellcounter):
	global total, purchaseLimit, BCC, USDT, jump, frequency, quantity, minute, ustdBalance, purchases

	if minute > len(data)-1: return

	market = getMarketSummary(mktcode)
	current = market['Last']
	
	if haveOpenOrders(mktcode):
		pass
	else:	
		if (ustdBalance>purchaseLimit*(1+0.0025)) and len(purchases)<8:
			if base < 0:
				base = current
			elif current < base:	
				base = current
			elif current < (base + jump):
				pass
			elif current >= (base + jump):
				base = current
				purchaseQuantity = purchaseLimit/current
				ustdBalance -= purchaseLimit*(1+0.0025)
				if buy(market, purchaseQuantity, current):
					purchase = current
					quantity = purchaseQuantity
					purchases.append(quantity)
					#print ustdBalance, purchases

		if len(purchases)>0:
			if current >= maximum:
				maximum = current
			else:
				notSold = []
				for quantity in purchases:
					purchase = purchaseLimit/quantity
					sufficientDown = ((maximum - current) > jump)#((maximum - current)/maximum > 0.01)#True
					profit = (current*quantity - purchaseLimit - current*quantity*0.0025 - purchaseLimit*0.0025)
					if (profit > 0 and sufficientDown):# or (purchase - current > 0.50*purchase):
						total += profit
						print minute, current, purchase, " profit/loss: "+str(profit)+" total:" + str(total)
						g.append(total)
						ustdBalance += quantity*current*(1-0.0025)
					else:
						notSold.append(quantity)	
				purchases = notSold[:]		

	sch.enter(frequency, 1, TradeMarket, (sch,mktcode,maximum,base, sellcounter))


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(frequency, 1, TradeMarket, (scheduler,mktcode,-1, -1, 12))
scheduler.run()

plt.plot(range(len(g)), g)
plt.ylabel('total profit')
plt.show()

