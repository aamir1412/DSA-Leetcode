class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1] * len(nums) 
        rp = [1] * len(nums) 
               
        pd = 1
        for i in range(1, len(nums)):
            lp[i] = nums[i-1] * pd
            pd = lp[i]
        
        nums = nums[::-1]        
        pd = 1
        for i in range(1, len(nums)):
            rp[i] = nums[i-1] * pd
            pd = rp[i]
        
        for i in range(len(nums)):
            nums[i] = lp[i] * rp[len(nums) - 1 - i]
        return nums