class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(k%len(nums)):
        #     temp = nums[-1]
        #     del(nums[-1])
        #     nums.insert(0,temp)
        # return nums

        # solution 2, very clever.
        # the rotated array's  first k nums will be the original array's last k arrays, and the order maintains.
        # so we first reverse the array, now the first k nums will the original last k nums, but with a reverse order
        # we just need to reverse the first k nums and the last n-k nums,
        # in this way, we only use  O(1) extra space, and only cost O(n) time.
        def reverse(start,end):
            while start < end:
                temp = nums[end]
                nums[end] = nums[start]
                nums[start] = temp
                end -= 1
                start += 1
        k = k%len(nums)
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)