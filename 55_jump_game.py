class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums)-1
        if not target:
            return True
        maximum = 0
        for i in range(target):
            maximum = max(maximum,i+nums[i])
            if maximum >= target:
                return True
            elif i == maximum:
                return False
            

            