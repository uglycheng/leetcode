class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        braket_dict = {
            "(":None,
            "{":None,
            "[":None,
            ")":"(",
            "}":"{",
            "]":"["
        }
        braket_stack = []
        for char in s:
            if braket_stack and (braket_stack[-1] == braket_dict[char]):
                braket_stack.pop()
            else:
                braket_stack.append(char)
        if len(braket_stack) == 0:
            return True
        else:
            return False