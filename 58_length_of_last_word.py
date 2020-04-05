class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in range(1,len(s)+1):
            if s[-i] != " ":
                length += 1
            elif length != 0:
                return length
        return length