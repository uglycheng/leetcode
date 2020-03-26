class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy
        perms = [[]]
        for i in range(len(nums)):
            sub_perm = len(perms)
            for j in range(sub_perm):
                for k in range(len(perms[0])+1):
                    perms.append(copy.copy(perms[0]))
                    perms[-1].insert(k,nums[i])
                del(perms[0])
        return perms


                

