class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            time = 0
            for b in piles:
                time += math.ceil(b / k) 
            if time <= h:
                return True
            else:
                return False
                
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            if eat(m):
                r = m - 1
            else:
                l = m + 1        
        return l