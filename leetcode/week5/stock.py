class Solution(object):
    def maxProfit(self, prices):
        min_buy = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)) :
            min_buy = min(prices[i], min_buy)            
            max_profit = max(max_profit, prices[i] - min_buy)

        return max_profit

print(Solution.maxProfit(Solution, [7,1,5,3,6,4]))
print(Solution.maxProfit(Solution, [7,6,4,3,1]))
 
