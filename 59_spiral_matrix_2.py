class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0 for i in range(n)] for top in range(n)]
        value = 1
        for top in range(n/2):
            for i in range(top,n-top):
                mat[top][i] = value
                value += 1  
            for i in range(top+1,n-top):
                mat[i][n-top-1] = value
                value += 1
            for i in range(n-top-2,top-1,-1):
                mat[n-top-1][i] = value
                value += 1
            for i in range(n-top-2,top,-1):
                mat[i][top] = value
                value += 1
        return mat

         

       
        
        