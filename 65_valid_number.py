class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isInteger(s):
            if s[0] == '+'  or s[0] == '-':
                s = s[1:]
            if len(s) ==  0:
                return False
            for digit in s:
                if not (ord('0')  <= ord(digit) <= ord('9')):
                    return False
            return True

        def isDecimal(s):
            if '.' not  in s:
                return False
            if s[0] == '+'  or s[0] == '-':
                s = s[1:]
            if len(s) <=1:
                return False
            pos_dot = s.find('.')
            left_part = s[:pos_dot]
            right_part = s[pos_dot+1:]
            for digit in left_part:
                if not (ord('0')  <= ord(digit) <= ord('9')):
                    return False
            for digit in right_part:
                if not (ord('0')  <= ord(digit) <= ord('9')):
                    return False
            return True

        def isScientific(s, delimiter):
            pos_deli = s.find(delimiter)
            if pos_deli == 0 or pos_deli == len(s)-1:
                return False
            left_part = s[:pos_deli]
            right_part = s[pos_deli+1:]
            return ((isDecimal(left_part) or isInteger(left_part)) and  isInteger(right_part))

        if 'e' in s:
            return isScientific(s,'e')
        elif 'E' in s:
            return isScientific(s,'E')
        else:
            return isInteger(s) or isDecimal(s)