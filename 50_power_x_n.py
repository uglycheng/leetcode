class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        positive = n >= 0
        ans = 1
        n = abs(n)
        while n > 0:
            if n%2:
                ans *= x 
                x *= x
                n = (n-1)/2
            else:
                x *= x
                n /= 2
        if positive:
            return ans
        else:
            return 1/ans

        # if you use C C++ Java, you may need to note the problem of overflow