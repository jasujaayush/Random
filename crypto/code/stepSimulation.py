import crypto_bot
import threading
import sched, time
import json
import matplotlib.pyplot as plt
import random

BCC = 'BTC'
USDT = 'USDT'
mktcode = 'USDT-BTC'
key = ""
secret = ""
api = crypto_bot.bittrex(key, secret)
ustdBalance = 410
purchaseLimit = 100
jump = 0.005
total = 0
frequency = 0.001 #seconds
quantity = 0
purchases = {}

data = json.load(open("BTC18DecOneMin.json"))["result"]
minute = 0
g = []

def getMarketSummary(mktcode):	
	global api,minute
	d = data[minute]
	minute += 1
	return d

def buy(market, quantity, rate):	
	return True

def sell(market, quantity, rate):	
	return True

def haveOpenOrders(market):
	False

def Bracket(current, purchases, market):
	intervals = (ustdBalance/purchaseLimit)
	window = 1000/intervals
	bracket = int(intervals - (19000 - current)/window)
	return bracket

def TradeMarket(sch, mktcode, maximum, base, sellcounter):
	global total, purchaseLimit, BCC, USDT, jump, frequency, quantity, minute, ustdBalance, purchases

	if minute > len(data)-1: return

	market = getMarketSummary(mktcode)
	current = market['C']
	#print current
	if haveOpenOrders(mktcode):
		pass
	else:	
		if (ustdBalance>purchaseLimit*(1+0.0025)):
			bracket =  Bracket(current, purchases, market)
			if base < 0 or current < base:
				base = current
			elif current < (base*(1+jump)):
				pass
			elif (current-base) >= base*jump and (bracket < 4) and (bracket >= 0) and (bracket not in purchases):
				base = current
				purchaseQuantity = purchaseLimit/current
				if buy(market, purchaseQuantity, current):
					ustdBalance -= purchaseLimit*(1+0.0025)
					purchase = current
					quantity = purchaseQuantity
					purchases[bracket] = purchaseQuantity
					#print ustdBalance, purchases

		if len(purchases)>0:
			tempProfit = 0
			if current >= maximum:
				maximum = current
			elif ((maximum - current) > maximum*jump): #sufficientDown
				for bracket in purchases:
					quantity = purchases[bracket]
					purchase = purchaseLimit/quantity	
					profit = (current*quantity - purchaseLimit - current*quantity*0.0025 - purchaseLimit*0.0025)
					if (profit > 0):
						total += profit
						tempProfit += profit
						ustdBalance += quantity*current*(1-0.0025)
						purchases[bracket] = 0

				for bracket,quantity in purchases.items():
					if quantity == 0:
						del purchases[bracket]

			if tempProfit>0:
				g.append(total)			
				print minute, current, purchase, " profit/loss: "+str(tempProfit)+" total:" + str(total)	

	sch.enter(frequency, 1, TradeMarket, (sch,mktcode,maximum,base, sellcounter))


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(frequency, 1, TradeMarket, (scheduler,mktcode,-1, -1, 12))
scheduler.run()

plt.plot(range(len(g)), g)
plt.ylabel('total profit')
plt.show()

