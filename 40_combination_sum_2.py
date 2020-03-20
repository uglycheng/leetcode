class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        # This if block makes sure line 20 didn't got bug at the beginning when current_trial[-1]==-1
        if candidates[0] == candidates[-1]:
            if target / candidates[0] * candidates[0] == target and target / candidates[0] <= len(candidates):
                return [[candidates[0]] * (target / candidates[0])]
            else:
                return []
        solution_set = []
        pre_sum = candidates[-1]
        current_trial = [-1]
        while current_trial:
            pre_sum -= candidates[current_trial[-1]]
            while current_trial[-1]+1 < len(candidates) and candidates[current_trial[-1]] == candidates[current_trial[-1]+1]:
                current_trial[-1] += 1
            current_trial[-1] += 1
            if current_trial[-1] == len(candidates):
                del[current_trial[-1]]
                continue
            pre_sum += candidates[current_trial[-1]]
            append_candidate = current_trial[-1] + 1
            if append_candidate < len(candidates):
                while pre_sum + candidates[append_candidate] <= target:
                    current_trial.append(append_candidate)
                    pre_sum += candidates[append_candidate]
                    append_candidate += 1
                    if append_candidate == len(candidates):
                        break
            pre_sum -= candidates[append_candidate - 1]
            while append_candidate < len(candidates) and pre_sum + candidates[append_candidate] <= target:
                current_trial[-1] = append_candidate
                append_candidate += 1
            if pre_sum + candidates[append_candidate-1] == target:
                solution_set.append([candidates[k] for k in current_trial])
            del(current_trial[-1])
        return solution_set

solution = Solution()
solution.combinationSum2([5,4,5,1,5,3,1,4,5,5,4],10)
            

