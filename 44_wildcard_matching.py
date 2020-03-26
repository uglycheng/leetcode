class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1,len(p)+1):
            dp[0][j] = (p[j-1] == "*" and dp[0][j-1])
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == "?" or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    # *represents character  or * represents 0 character
                #print(str(i)+", "+str(j)+"  " + str(dp[i][j]))
        return dp[-1][-1]

        # i = 0
        # j = 0
        # start = -1
        # match = 0
        # while i < len(s):
        #     # 一对一匹配,匹配成功一起移
        #     if j < len(p) and (s[i] == p[j] or p[j] == "?"):
        #         i += 1
        #         j += 1
        #     # 记录p的"*"的位置,还有s的位置
        #     elif j < len(p) and p[j] == "*":
        #         start = j
        #         match = i
        #         j += 1
        #     # j 回到 记录的下一个位置
        #     # match 更新下一个位置
        #     # 这不代表用*匹配一个字符
        #     elif start != -1:
        #         j = start + 1
        #         match += 1
        #         i = match
        #     else:
        #         return False
        #  # 将多余的 * 直接匹配空串
        # return all(x == "*" for x in p[j:])


solution = Solution()
solution.isMatch("abceb","*a*b")