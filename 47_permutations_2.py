class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy
        #re-order nums
        last_same_num = {}
        for i in range(len(nums)):
            if nums[i] in last_same_num.keys():
                last_same_num[nums[i]] += 1
            else:
                last_same_num[nums[i]] = 1
        nums = []
        for key, value in last_same_num.items():
            nums += [key for i in range(value)]    
        # this step is to help line 25 works when i=0
        if nums[0] == nums[-1]:
            return [nums]        
        # main part
        perm = [[]]
        for i in range(len(nums)):
            sub_perm = len(perm)
            if nums[i] != nums[i-1]:
                last_same_num = [-1 for j in range(sub_perm)]
            for j in range(sub_perm):
                for k in range(last_same_num[0]+1, len(perm[0])+1):
                    perm.append(copy.copy(perm[0]))
                    perm[-1].insert(k,nums[i])
                    last_same_num.append(k)
                del(perm[0])
                del(last_same_num[0])
        return perm

solution = Solution()
solution.permuteUnique([3,3,1,2,3,2,3,1])