class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        else:
            pt = [[1]]
        for i in range(1,numRows):
            next_line = [1]
            for j in range(i-1):
                next_line.append(pt[i-1][j]+pt[i-1][j+1])
            next_line.append(1)
            pt.append(next_line)
        return pt