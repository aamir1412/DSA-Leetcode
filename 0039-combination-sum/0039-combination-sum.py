class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, com = [], []
        def dfs(idx, total):
            if total > target or idx >= len(candidates):
                return
            
            if total == target:
                res.append(com.copy())
                return
            
            com.append(candidates[idx])
            dfs(idx, candidates[idx] + total)
            com.pop()
            dfs(idx + 1, total)
            
        dfs(0, 0)
        return res
            
        