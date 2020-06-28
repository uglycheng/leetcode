class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This is a implementation of official solution
        if 1 not in nums:
            return 1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        for i in range(n):
            value = abs(nums[i])
            nums[value-1] = -abs(nums[value-1])

        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1
