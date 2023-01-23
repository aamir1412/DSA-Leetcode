class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        d = defaultdict(list)        
        for i in range(len(nums)):
            d[nums[i]].append(i)        
        
        maxx = 0
        res = len(nums)
        for key in d:
            v = d[key]
            if len(v) > maxx:
                maxx = len(v)
                res = (v[-1] - v[0] + 1)
            elif len(v) == maxx:
                res = min(res, (v[-1] - v[0] + 1))
        return res        