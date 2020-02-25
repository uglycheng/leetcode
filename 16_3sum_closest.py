class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float("inf")
        sum_closet = 0
        for i in range(len(nums)-2):
            # i is the target index, j and k are double pointers
            if nums[i] == nums[i-1] and i != 0:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                distance = target - three_sum
                distance_abs = abs(distance)
                if distance_abs < closest:
                    closest = distance_abs
                    sum_closet = three_sum
                if distance == 0 : 
                    return sum_closet
                elif distance > 0:
                    j += 1
                else:
                    k -= 1  
        return sum_closet

        

