class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        for x in range (len(nums1)):
            if i>=n:
                break
            if nums1[x]==0:
                nums1[x]=nums2[i]
                i+=1
        nums1.sort()
    
