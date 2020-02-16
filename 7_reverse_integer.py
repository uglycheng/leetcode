class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 0x7fffffff
        min = -2**31 #in python, you can not use 0x80000000
        reverse = 0
        if x>0:
            sign=1
        elif x<0:
            sign=-1
        else:
            return 0
        x *= sign
        while x>0:
            reverse = (reverse*10)+(x%10)
            x /= 10
        reverse *= sign
        if reverse>max or reverse<min:
            return 0
        else:
            return reverse

solution = Solution()
print(solution.reverse(123))