class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for x in nums:
            dct[x] = 1 + dct.get(x, 0)
        
        fq = [[] for i in range(len(nums) + 1)]
        for x in dct:
            idx = dct[x]
            fq[idx].append(x)
        
        res = []
        for i in range(len(nums), -1, -1):
            if k == len(res):
                return res
            if fq[i]:
                for n in fq[i]:
                    res.append(n)
                  
                
            
        