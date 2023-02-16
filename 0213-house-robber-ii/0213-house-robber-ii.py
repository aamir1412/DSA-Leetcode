class Solution:
    def rob(self, nums: List[int]) -> int:           
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        def rob(idx, n):
            pin, pex = nums[idx], 0
            for i in range(idx+1, n):
                cin = nums[i] + pex
                cex = max(pin, pex)
                pin, pex = cin, cex
            return cin, cex
        
        
        # 1st house included
        inc, exc = rob(0, n-1)
        fmax = max(inc, exc)
        
        # 2nd house included
        inc, exc = rob(1, n)
        smax = max(inc, exc)
        
        return max(fmax, smax)