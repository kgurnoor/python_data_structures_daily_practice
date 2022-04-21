class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(mat) * len(mat[0]):
            return mat
        new_mat = [[] for _ in range(r)]
        k = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(new_mat[k]) == c:
                    k += 1
                new_mat[k].append(mat[i][j])
        return new_mat
