class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pt_generated = {"(":[1,0]}
        str_len = 1
        while str_len < 2*n :
            newly_generated = {}
            for combination in pt_generated.keys():
                pt_uesd = pt_generated[combination]
                if pt_uesd[0] > pt_uesd[1]:
                    newly_generated[combination+")"] = [pt_uesd[0],pt_uesd[1]+1]
                if pt_uesd[0] < n :
                    newly_generated[combination+"("] = [pt_uesd[0]+1,pt_uesd[1]]
            pt_generated = newly_generated
            str_len += 1
        return list(pt_generated.keys())

solution = Solution()
print(solution.generateParenthesis(3))

