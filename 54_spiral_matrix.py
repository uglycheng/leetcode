class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        result = []
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        while top < bottom and left<right:
            for j in range(left,right):
                result.append(matrix[top][j])
            top += 1
            for i in range(top,bottom):
                result.append(matrix[i][j])
            right -= 1
            if top < bottom:
                for j in range(right-1,left-1,-1):
                    result.append(matrix[i][j])
            bottom -= 1
            if left < right:
                for i in range(bottom-1,top-1,-1):
                    result.append(matrix[i][j])
            left += 1
        return result


