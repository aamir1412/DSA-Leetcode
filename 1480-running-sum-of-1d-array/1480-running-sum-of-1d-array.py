class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = [0] * (len(nums) + 1)        
        for i in range(1, len(nums)+1):
            res[i] = (res[i-1] + nums[i-1])                        
        
        return res[1:]
            