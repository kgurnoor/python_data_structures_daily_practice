class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        :nums is the array
        :define a function with 'nums' as the input, returns a boolean value
        :function goes through every element, identifies if any element appears more than once
        :sort it in ascending/descending order
        :use 'for i in nums' to go through every element in the array
        :if the preceding element is equal to the current element, return true
        :if not, move to the next element and repeat
        :if reached end, return false

        """
        nums.sort()
        p=nums[0]
        for i in nums[1:]:
            if i == p:
                return True
            p = i
        return False




        
