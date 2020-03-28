class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        max_index = len(matrix) - 1
        for i in range(len(matrix)/2):
            for j in range(i,max_index-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[max_index-j][i]
                matrix[max_index-j][i] = matrix[max_index-i][max_index-j]
                matrix[max_index-i][max_index-j] = matrix[j][max_index-i]
                matrix[j][max_index-i] = temp