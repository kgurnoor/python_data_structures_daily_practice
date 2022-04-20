class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ht = dict()

        longer = []
        smaller = []
        intersection = []
        if len(nums1) > len(nums2):
            longer = nums1
            smaller = nums2
        else:
            longer = nums2
            smaller = nums1

        for i in range(len(longer)):
            if longer[i] in ht:
                ht[longer[i]] = ht[longer[i]]+1
            else:

                ht[longer[i]] = 1


        for j in range(len(smaller)):
            if smaller[j] in ht and ht[smaller[j]]>0:
                intersection.append(smaller[j])
                ht[smaller[j]] = ht[smaller[j]]-1


        return intersection

        
