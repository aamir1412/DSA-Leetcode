class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:       
        #my code
        res, cur = [], []        
        
        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())                
                return
            
            for i in nums:
                if i in cur:
                    continue
                cur.append(i)
                dfs()
                cur.pop()
                        
        dfs()            
        return res