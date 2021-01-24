class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        num_cols = len(matrix[0])
        xor_mat = [0 for i in range(len(matrix)*len(matrix[0]))]
        xor_mat[0] = matrix[0][0]
        for i in range(1,len(matrix)):
            xor_mat[i*num_cols] = matrix[i][0] ^ xor_mat[(i-1)*num_cols]
        for j in range(1,len(matrix[0])):
            xor_mat[j] = matrix[0][j] ^ xor_mat[j-1]
        for i in range(1,len(matrix)):
            for j in range(1,num_cols):
                xor_mat[i*num_cols+j] = xor_mat[(i-1)*num_cols+(j-1)]^ \
                                        xor_mat[i*num_cols+(j-1)]^ \
                                        xor_mat[(i-1)*num_cols+j]^ \
                                        matrix[i][j]

        import heapq
        return heapq.nlargest(k,xor_mat)[-1]
        # if k < len(matrix) * num_cols / 2:
        #     for i in range(k-1):
        #         xor_mat[xor_mat.index(max(xor_mat))] = -1
        #     return max(xor_mat)
        # else:
        #     k = len(matrix) * num_cols - k+1
        #     for i in range(k-1):
        #         xor_mat[xor_mat.index(min(xor_mat))] = 'inf'
        #     return min(xor_mat)
            
