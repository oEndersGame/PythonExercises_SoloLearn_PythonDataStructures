# Problem:
'''
You are analyzing house prices. The given code declares a list with house prices in the neighborhood.
You need to calculate and output the number of houses that have a price that is above the average.

To calculate the average price of the houses, you need to divide the sum of all prices by the number of houses.

NOTE: Use sum(list) to calculate the sum of all items in the list and len(list) to get the number of items.
'''
#--------------------------------------------#

# CODE:

prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]

#your code goes here
average = sum(prices)/len(prices)

above_ave = 0
count = 0
for i in prices:
    count += 1
	if i > average:
		above_ave += 1

print(above_ave)