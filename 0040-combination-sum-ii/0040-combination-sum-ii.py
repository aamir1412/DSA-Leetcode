class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []    
        cur = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i+1, cur, total+nums[i])
            
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            cur.pop()
            dfs(i+1, cur, total)
            
        dfs(0, [], 0)
        return res
        