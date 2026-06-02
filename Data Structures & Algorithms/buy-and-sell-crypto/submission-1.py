class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        highest = prices[n-1]
        vals = [highest]
        for i in range(n-2,-1,-1):
            highest = max(highest,prices[i])
            vals.append(highest)
        
        vals.reverse()
        
        p = 0
        for i in range(n):
            p = max(p,vals[i]-prices[i])
        
        
        return p




        