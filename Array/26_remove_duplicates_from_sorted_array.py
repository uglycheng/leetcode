class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                i += 1
            else:
                del(nums[i])
        return i
