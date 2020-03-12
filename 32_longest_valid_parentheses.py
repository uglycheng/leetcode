class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Rule 1: Any string that begin with a substring which has more ")" than "(" is not a valid string 

        ##Dynamic Programming
        dp={0:0}
        maxlen = 0
        if len(s) < 2:
            return 0
        if s[0:2] == "()":
            dp[1] = 2
            maxlen = 2
        else:
            dp[1] = 0
        for i in range(2,len(s)):
            if s[i] == "(":
                dp[i] = 0
            elif s[i-1] == "(":
                dp[i] = dp[i-2]+2
            elif s[i-1] == ")" and i-dp[i-1]>0 and s[i-dp[i-1]-1] == "(":
                dp[i] = dp[i-1] + 2
                if i-dp[i-1]>1:
                    dp[i] += dp[i-dp[i-1]-2]
            # it can be proved when s[i-dp[i-1]-1] == ")", dp[i] should be 0
            # firstly, the final ")" cannot cover a valid string with a "(" within substriing dp[i-1], 
            # for otherwise the sub-substring of dp[i-1] before the "(" will have one more ")" than "(", acorrding to rule1, it's impossible
            # second, the final ")" cannot cover a valid string with a "(" before substring dp[i-1]
            # for otherwise there must be another "(" to match with the s[i-dp[i-1]-1] == ")", then dp[i-1] is not the longest. 
            else:
                dp[i] = 0
            if dp[i] > maxlen:
                maxlen = dp[i]
        return maxlen

        # # Using Stack
        # stack = [-1]  #the stack 
        # maxlen = 0
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         stack.append(i)
        #     elif s[i] == ")":
        #         stack.pop()
        #         if len(stack) == 0:
        #             stack.append(i)
        #         else:
        #             maxlen = max(maxlen,i-stack[-1])
        # return maxlen

        # # Bidirectional Traversal
        # left = 0
        # right = 0
        # maxlen = 0
        # for i in range(len(s)):
        #     if s[i] == ")":
        #         right += 1
        #     else:
        #         left += 1
        #     if right > left:
        #         left = 0
        #         right = 0
        #     elif right == left:
        #         maxlen = max(maxlen,2*left)
        # left = 0
        # right = 0
        # for i in range(-1, -len(s)-1, -1):
        #     if s[i] == ")":
        #         right += 1
        #     else:
        #         left += 1
        #     if right < left:
        #         left = 0
        #         right = 0
        #     elif right == left:
        #         maxlen = max(maxlen,2*left)
        # return maxlen
        