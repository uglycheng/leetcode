class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums) - 1
        if tail == -1: 
            return 0
        elif nums[head] == target:
            return head
        elif nums[tail] == target:
            return tail
        elif nums[head] > target:
            return 0 
        elif nums[tail] < target:
            return tail + 1
        while head < tail - 1:
            mid  = (head + tail) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid
            else:
                head = mid
        return tail
