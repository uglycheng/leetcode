class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            # i is the target index, j and k are double pointers
            if nums[i] == nums[i-1] and i != 0:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                sumjk = nums[j] + nums[k]
                if sumjk == -nums[i]: 
                    triplets.append([nums[i],nums[j],nums[k]]) 
                    j += 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                elif sumjk < -nums[i]:
                    j += 1
                else:
                    k -= 1           
        return triplets

        # #this solution use i j as double pointers and find whether their minus sum are in the nums and bigger than nums[j+1] to avoid duplicate
        # nums.sort()
        # hashmap = {}
        # for num in nums:
        #     hashmap[num] = True
        # i = 0 
        # j = 1
        # triplets = []
        # for i in range(len(nums)-2):
        #     if nums[i] == nums[i-1] and i != 0:
        #         continue
        #     for j in range(i+1, len(nums)-1):
        #         if nums[j] == nums[j-1] and j != i+1:
        #             continue
        #         minus_2sum = -nums[i]-nums[j] 
        #         if (minus_2sum in hashmap) and (minus_2sum >= nums[j+1]):
        #             triplets.append([nums[i],nums[j],minus_2sum])
        # return triplets

