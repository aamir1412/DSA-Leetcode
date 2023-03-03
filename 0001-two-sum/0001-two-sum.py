class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = 0
        dct = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in dct:
                return [i, dct[d]]
            dct[nums[i]] = i