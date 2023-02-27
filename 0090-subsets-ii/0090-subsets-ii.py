class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sub = [], []
        nums.sort()
        def dfs(idx):
            if idx >= len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[idx])
            dfs(idx + 1)
            sub.pop()
            while(idx < len(nums) - 1 and nums[idx] == nums[idx+1]):                
                idx+=1                
            dfs(idx + 1)
            
        dfs(0)
        return res