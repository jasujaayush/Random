import crypto_bot
import threading
import sched, time
import json
import matplotlib.pyplot as plt
import random
import sys

#Example Run from "crypto" folder: python2.7 code/simulated.py data/BTC5min1Dec.json 1

BCC = 'BTC'
USDT = 'USDT'
mktcode = 'USDT-BTC'
key = ""
secret = ""
api = crypto_bot.bittrex(key, secret)
purchaseLimit = 200
total = 0
jump = float(sys.argv[2])/100
frequency = 0.001 #seconds
quantity = 0
file = sys.argv[1]
data = json.load(open(file))["result"]
minute = 0
g = []

def getMarketSummary(mktcode):	
	global api,minute
	d = {'Last':data[minute]['H']}
	minute += 1
	return d

def buy(market, quantity, rate): return True

def sell(market, quantity, rate): return True

def haveOpenOrders(market): False

def TradeMarket(sch, mktcode, maximum, base, jump):
	global total, purchaseLimit, BCC, USDT, frequency, quantity, minute

	if minute > len(data)-1: return

	market = getMarketSummary(mktcode)
	current = market['Last']
	
	if haveOpenOrders(mktcode):
		pass
	elif quantity <= 0:
		if base < 0 or current < base:
			base = current
		elif current < (base*(1+jump)):
			pass
		elif current >= (base*(1+jump)):
			purchaseQuantity = purchaseLimit/current
			if buy(market, purchaseQuantity, current):
				maximum = current
				purchase = current
				quantity = purchaseQuantity
	else:
		if current >= maximum:
			maximum = current
		else:
			purchase = purchaseLimit/quantity
			sufficientDown = current < maximum*(1-jump)
			profit = (current*quantity - purchaseLimit - current*quantity*0.0025 - purchaseLimit*0.0025)
			if (profit > 0 and sufficientDown):
				total += profit
				print minute, current, purchase, " profit/loss: "+str(profit)+" total:" + str(total)
				g.append(total)
				base = -1
				maximum = -1
				purchase = -1
				quantity = 0
			else:	
				pass

	sch.enter(frequency, 1, TradeMarket, (sch,mktcode,maximum,base, jump))


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(frequency, 1, TradeMarket, (scheduler,mktcode,-1, -1, jump))
scheduler.run()

plt.plot(range(len(g)), g)
plt.ylabel('total profit')
plt.show()

