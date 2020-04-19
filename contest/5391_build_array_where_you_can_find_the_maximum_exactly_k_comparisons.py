class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        # dp[i][j][c] represents in first i nums, cost is j,  max is c, then how  many  possible array  exist.
        dp=[[[0 for c in range(m)] for j in range(k+1) ] for i in range(n+1)]
        dp[1][1] = [1 for c in range(1,m+1)]
        for i in range(2,n+1):
            for j in range(1,min(k+1,i+1)):
                for c in range(m):
                    # two situations, the maximum c is the last num, or not
                    dp[i][j][c] = sum(dp[i-1][j-1][:c])  + dp[i-1][j][c]  * (c+1)
                    #print(str(i)+", "+str(j)+", "+str(c)+": "+str(dp[i][j][c]))
        return sum(dp[n][k])%(10**9+7)
