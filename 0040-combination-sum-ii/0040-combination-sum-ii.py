class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, cur = [], []
        candidates.sort()
        def dfs(idx, total):
            if total == target:
                res.append(cur.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            
            cur.append(candidates[idx])
            dfs(idx+1, candidates[idx] + total)  
            cur.pop()
            while(idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]):
                idx += 1            
            dfs(idx+1, total)
            
        dfs(0, 0)
        return res
            
        