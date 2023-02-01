class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        lcs = 0
        for n in nums:
            if n-1 not in numset:
                count = 0                
                while n in numset:
                    n += 1  
                    count += 1
                lcs = max(lcs, count)
        return lcs                
                