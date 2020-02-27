class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        anws = []
        for i in range(len(nums)-3):
            if nums[i] == nums[i-1] and i != 0:
                continue
            for j in range(i+1, len(nums)-2):
                if nums[j] == nums[j-1] and j != i+1:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l :
                    four_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if four_sum == target:
                        anws.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        l -= 1
                        while nums[k] == nums[k-1] and k < l :
                            k += 1
                    elif four_sum > target:
                        l -= 1
                    else:
                        k += 1
        return anws