class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)        
        for s in strs:
            count = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                count[idx] += 1
            dct[tuple(count)].append(s)
                
        res = []
        for k in dct:
            res.append(dct[k])
        return res