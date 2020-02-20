class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0: return ""
        common_prefix = strs[0]
        for string in strs[1:]:
            potential_max_len = min(len(common_prefix), len(string))
            if potential_max_len == 0:
                return ""
            common_prefix = common_prefix[:potential_max_len]
            for i in range(potential_max_len):
                if string[i] != common_prefix[i]:
                    common_prefix = common_prefix[:i]
                    break
        return common_prefix

        # #Below are two solutions from user xshura
        # #Solution 1
        # def longestCommonPrefix(self, strs):
        #     if not strs: return ""
        #     s1 = min(strs)
        #     s2 = max(strs)
        #     for i,x in enumerate(s1):
        #         if x != s2[i]:
        #             return s2[:i]
        #     return s1
        # #Solution 2
        # def longestCommonPrefix(self, strs):
        #     if not strs: return ""
        #     ss = list(map(set, zip(*strs)))
        #     res = ""
        #     for i, x in enumerate(ss):
        #         x = list(x)
        #         if len(x) > 1:
        #             break
        #         res = res + x[0]
        #     return res
        



solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))