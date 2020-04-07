class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = 1
        for i in range(2,n):
            factorial *= i
        nums = [str(i) for i in range(1,n+1)]
        ans = ""
        for i in range(n-1,0,-1):
            num = (k-1)/factorial
            k = k%factorial
            ans += nums[num]
            del(nums[num])
            if k==0:
                break
            factorial /= i
        for i in range(len(nums)-1,-1,-1):
            ans += nums[i]
        return ans
