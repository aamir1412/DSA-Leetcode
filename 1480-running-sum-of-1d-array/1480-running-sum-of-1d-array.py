class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = []
        sum = 0
        for i in range(len(nums)):
            res.append((sum + nums[i]))
            sum = res[-1]
            
        return (res)
            