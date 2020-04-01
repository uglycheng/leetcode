class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pointer i for the beginning index of the interval
        # pointer j for the end index  of the interval
        # if sum(nums[i:j+1]) > 0, then this interval nums[i:j+1] should be included when considering following intervals, 
        # because they would have positive contribution 
        # otherwise, this interval shouldn't been included, just explore from nums[j+1]
        # you may worry that should we give up nums[i:j+1] completely? Maybe the sub-interval nums[k:j+1] where i< k kwould have positive contribution?
        # this is impossible, because we have see every nums[i:k] and they are positive, otherwise you won't reach j, 
        # so if sum(nums[i:j+1]) <= 0, then sum(nums[k:j+1]) must be smaller than sum(nums[i:j+1])
        i = 0
        j = 0
        maximum = -float('inf')
        sum_nums = 0
        while j<len(nums):
            sum_nums += nums[j]
            maximum = max(sum_nums,maximum)
            if sum_nums <= 0:
                sum_nums = 0
                i = j+1
            j += 1
        return maximum

s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
