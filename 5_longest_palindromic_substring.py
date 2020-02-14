class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ################### Dynamic Programming #####################
        #is_plaindrome = [[None for i in range(len(s))] for j in range(len(s))]
        is_plaindrome = [[None for i in range(len(s))] for j in range(len(s))]
        longest_head, longest_tail, longest_length = 0, 0, 1
        if len(s) == 0:
            return s
        else:
            is_plaindrome[0][0] = True
        for tail in range(1,len(s)):
            is_plaindrome[tail][tail] = True
            for head in range(tail-1):
                if (s[head]==s[tail]) and is_plaindrome[head+1][tail-1]:
                    is_plaindrome[head][tail] = True
                    if tail - head + 1 > longest_length:
                        longest_head, longest_tail, longest_length = head, tail, tail-head+1
            if s[tail-1] == s[tail]:
                is_plaindrome[tail-1][tail] = True
                if 2 > longest_length:
                    longest_head, longest_tail, longest_length = tail-1, tail, 2
        return s[longest_head:longest_tail+1]

solution = Solution()
print(solution.longestPalindrome("aaabaaaa"))

