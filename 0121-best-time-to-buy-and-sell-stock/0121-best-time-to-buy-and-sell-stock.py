class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        l, r = 0, 0
        
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            if prices[r] - prices[l] > maxx:
                maxx = ( prices[r] - prices[l] )                           
            r += 1
        return maxx                