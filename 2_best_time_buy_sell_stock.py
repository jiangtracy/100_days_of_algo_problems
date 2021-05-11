'''
input: list of prices
output: highest profit, or 0

- declare a var to keep track of current lowest price
- declare another var for highest profit at the moment
- iterate over the prices
- update lowest price and highest profit at each iteration
- return the highest profit if it's greater than 0
- otherwise return 0
    
time complexity: O(n)
space complexity O(1)

leetcode #121

'''


def maxProfit(prices):
    lowestPrice = prices[0]
    highestProfit = 0
    
    for price in prices:
        if price < lowestPrice:
            lowestPrice = price 
        
        currentProfit = price - lowestPrice
        
        if currentProfit > highestProfit:
            highestProfit = currentProfit
    
    return 0 if highestProfit <= 0 else highestProfit
    
