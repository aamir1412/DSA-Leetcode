class Solution:
    def rob(self, nums: List[int]) -> int:        
        prev_exc, prev_inc = 0, 0
        
        for x in nums:
            cur_inc = x + prev_exc
            cur_exc = max(prev_inc, prev_exc)
            prev_exc, prev_inc = cur_exc, cur_inc
            
        return max(cur_inc, cur_exc)