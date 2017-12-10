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
purchaseLimit = 200
jump = 10.0
total = 0
frequency = 0.001 #seconds
quantity = 0

data = json.load(open("GetTicksBTC30.json"))["result"]
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
	global total, purchaseLimit, BCC, USDT, jump, frequency, quantity, minute

	if minute > len(data)-1: return

	market = getMarketSummary(mktcode)
	current = market['Last']
	
	if haveOpenOrders(mktcode):
		pass
	elif quantity <= 0:
		if base < 0:
			base = current
		elif current < base:	
			base = current
		elif current < (base + jump):
			pass
		elif current >= (base + jump):
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
			sufficientDown = True#((maximum - current)/maximum > 0.01)#((maximum - current) > jump)#((maximum - current)/maximum > 0.01)#True#
			if (maximum - current > 0.10*maximum):
				sellcounter -= 1
			profit = (current*quantity - purchaseLimit - current*quantity*0.0025 - purchaseLimit*0.0025)
			if (profit > 0 and sufficientDown):# or (purchase - current > 0.50*purchase):
				total += profit
				print minute, current, purchase, " profit/loss: "+str(profit)+" total:" + str(total)
				g.append(total)
				base = -1
				maximum = -1
				purchase = -1
				sellcounter = 60
				quantity = 0
			else:	
				pass

	sch.enter(frequency, 1, TradeMarket, (sch,mktcode,maximum,base, sellcounter))


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(frequency, 1, TradeMarket, (scheduler,mktcode,-1, -1, 12))
scheduler.run()

plt.plot(range(len(g)), g)
plt.ylabel('total profit')
plt.show()

