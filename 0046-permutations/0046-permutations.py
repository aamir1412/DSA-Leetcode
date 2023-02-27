class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, perm = [], []
        def dfs():            
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in nums:
                if i in perm:
                    continue
                perm.append(i)
                dfs()
                perm.pop()
            
        dfs()
        return res
        
        