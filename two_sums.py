class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for cnt, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target-num], cnt
            lookup[num] = cnt  
