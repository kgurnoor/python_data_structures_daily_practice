class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m,n = len(matrix), len(matrix[0])
        low = 0
        high = (m * n) -1
        while low <= high:
            mid = (low+high)//2
            midElement = matrix[mid//n][mid%n]
            if midElement == target:
                return True
            elif midElement > target:
                high = mid -1
            else:
                low = mid + 1
        return False
