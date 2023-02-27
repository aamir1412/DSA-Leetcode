class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res, sub = [], []
        
        def dfs(idx):            
            if idx >= len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[idx])
            dfs(idx+1)
            sub.pop()
            dfs(idx+1)
        
        dfs(0)
        return res
        