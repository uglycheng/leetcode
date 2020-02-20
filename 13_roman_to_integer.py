class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,"":0}
        integer = 0
        while len(s) >= 2:
            if dictionary[s[0]] < dictionary[s[1]]:
                integer += (dictionary[s[1]] - dictionary[s[0]])
                s = s[2:]
            else:
                integer += dictionary[s[0]]
                s = s[1:]
        integer += dictionary[s]
        return integer
