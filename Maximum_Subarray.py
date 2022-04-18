class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        :find two such postive number which have maximum number of positive number in between them
        :use 'for i in nums'
        :
        """
        sumVal = 0
        ret = 0
        for i in nums:
            sumVal = max(0, sumVal) + i
            ret = max(ret, sumVal)
        return max(nums) if ret == 0 else ret
