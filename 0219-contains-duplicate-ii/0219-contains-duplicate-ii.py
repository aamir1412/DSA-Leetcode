class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
                
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
                
        for key in d:
            v = d[key]
            
            if len(v) > 1:                                
                for i in range(len(v)-1):                    
                    if ((v[i+1] - v[i]) <= k):                        
                        return True
                    