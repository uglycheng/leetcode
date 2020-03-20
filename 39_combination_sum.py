class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        solution_set = []
        current_trial = [-1]
        pre_sum = candidates[current_trial[-1]]
        while current_trial:
            pre_sum -= candidates[current_trial[-1]]
            current_trial[-1] += 1
            final_num = current_trial[-1]
            pre_sum += candidates[final_num]
            while pre_sum + candidates[final_num] <= target:
                current_trial.append(final_num)
                pre_sum += candidates[final_num]
            i = final_num
            pre_sum -= candidates[final_num]
            while pre_sum + candidates[i] <= target:
                current_trial[-1] = i
                i += 1
                if i == len(candidates):
                    break
            if pre_sum + candidates[i-1] == target:
                solution_set.append([candidates[k] for k in current_trial])
            del(current_trial[-1])
            while current_trial and current_trial[-1] == len(candidates) - 1:
                pre_sum -= candidates[current_trial[-1]]
                del(current_trial[-1])
        return solution_set

solution = Solution()
print(solution.combinationSum([7,3,2],18))