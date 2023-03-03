class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for n in nums:
            numset.add(n)
        maxx = 0            
        for x in nums:
            if x - 1 not in numset:
                count = 0
                n = x
                while n in numset:
                    n += 1
                    count += 1
                maxx = max(maxx, count)
        return maxx