class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        head, ans = 0, 0
        for j in range(len(s)):
            if s[j] in chars:
                head = max(chars[s[j]],head)
            ans = max(ans,j-head+1)   #here add one because in next line j add one
            chars[s[j]] = j+1         #here add one in order to deal with the case "" an empty string, if not add one ans will be 0, if add ans will be 1, leetcode ans is 1 
        return ans