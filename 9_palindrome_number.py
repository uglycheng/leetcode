class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        forward = x
        
        reverse = 0
        while x > 0:
            reverse = (reverse*10) + x%10
            x /= 10
        
        #reverse = int(str(forward)[::-1])
        
        if forward == reverse:
            return True
        else:
            return False