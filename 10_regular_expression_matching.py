class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[None for i in range(len(p)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = False
        dp[0][0] = True
        for j in range(len(p)):
            dp[0][j+1] = (p[j]=="*" and dp[0][j-1] and j>0) # s="" ,p="a*b*c*"
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == "*":
                    dp[i+1][j+1] = dp[i+1][j-1]  or  (dp[i][j-1] and (s[i]==p[j-1] or p[j-1]=="."))  or  (dp[i][j+1] and (s[i]==p[j-1] or p[j-1]==".")) 
                                  #(p[j-1] no repeat)   or           (p[j-1] repeat for once)             or      (p[j-1] repeat for many times)
                else:
                    dp[i+1][j+1] = dp[i][j] and (s[i]==p[j] or p[j]==".")
                #print(str(i+1)+" "+str(j+1)+ " "+ str(dp[i+1][j+1])) 
        return dp[len(s)][len(p)]

solution = Solution()
print(solution.isMatch("aab","c*a*b"))