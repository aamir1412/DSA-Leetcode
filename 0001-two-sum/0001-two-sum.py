class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        res = []
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hmap:
                res.append(i)
                res.append(hmap[dif])
                return res
            else:                
                hmap[nums[i]] = i     
         
                