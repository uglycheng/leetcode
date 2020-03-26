class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Dynamic Programming, unfortunately it's too slow
        # nums.reverse()
        # dp = [0]
        # for i in range(1,len(nums)):
        #     if nums[i]:
        #         dp.append(min(dp[max(0,i-nums[i]):i])+1)
        #     else:
        #         dp.append(float("inf"))
        # return dp[-1]

        # #early termination
        # if len(nums)==1:
        #     return 0
        # max_dis = 0
        # end_of_these_steps = 0
        # step_count = 0
        # for i in range(len(nums)-1):
        #     max_dis = max(nums[i]+i,max_dis)
        #     if max_dis >= len(nums)-1:
        #         return step_count+1
        #     if i == end_of_these_steps:
        #         end_of_these_steps = max_dis
        #         step_count += 1
        # return step_count


    
        max_dis = 0
        end_of_these_steps = 0
        step_count = 0
        for i in range(len(nums)-1):
            max_dis = max(nums[i]+i,max_dis)
            if i == end_of_these_steps:
                end_of_these_steps = max_dis
                step_count += 1
        return step_count