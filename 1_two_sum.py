class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another = target - num
            if another in hashmap:
                return [hashmap[another], index]
            else:
                hashmap[num] = index
        return None