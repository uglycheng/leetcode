class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #The idea is, looking from the tail of the list to find a[i] > a[i-1], when we find this i,
        #it means elements after i are in a descending order, then we check them one by one to find a a[i+k]<=a[i-1]
        #if we find it ,then swap a[i+k-1] and a[i-1], if not, swap a[i+kmax] and a[i-1]
        #then reverse the elements after i-1
        if len(nums)== 1:
            return  
        for i in range(-1,-len(nums),-1):
            if nums[i] > nums[i-1]:
                for k in range(0,-i):
                    if nums[i+k] <= nums[i-1]:
                        k -= 1 
                        break
                # k coming from the break of coming from end of for loop should be processed in a different way, k-=1 before break solve this problem
                temp = nums[i+k]
                nums[i+k] = nums[i-1]
                nums[i-1] = temp
                i = len(nums)+i  
                break
        if i < 0:
            i = 0  
        for j in range(i,len(nums)-1):
            temp = nums.pop()
            nums.insert(j,temp)


solution = Solution()
solution.nextPermutation([1,5,1])
        
             
            