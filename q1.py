"""
Question 1

Meera is a real estate investor. She is known for her excellent sense of timing when it comes to buying and selling properties. Meera always buys property at a low price and sells it at a high price to ensure the maximum profit. However, Meera never buys a property if the price is constantly going down.

As an analyst, your job is to calculate the maximum profit Meera could have made based on the property prices each day. If prices only decrease over time, Meera does not make any purchases.

"""

# Reading n 
n = int(input())

# Reading n input for prices
prices = list()
for i in range(n):
    prices.append(int(input()))


min_price = prices[0] # Initializing min_price as first element and profit as 0
profit = - 1
sell = 0


for cur in prices:
    if cur < min_price: # Finding the minimum price
        min_price = cur
    if cur - min_price > profit: # Finding the max profit by selling with the maximum price
        sell = cur
        profit = cur - min_price

if profit != -1:
    print(f'\nProfit: {profit}')
    # print(f'Bought on {min_price} and got sold on {sell}')
else:
    print("Meera never bought, as prices are going down..")

"""
Sample Input for Custom Testing

Sample Input: 6, [5, 10, 3, 9, 1, 8]
Sample Output: 7

Explanation:
The maximum profit possible is when Meera buys the property at 3 and sells it at 10, resulting in a profit of 7.

"""
# Assuming the prices are for each day, Meera cannot sell for 10 as its previous day 
# So the answer will be buying on 1 and selling on 10, yielding the same 7 as profit 