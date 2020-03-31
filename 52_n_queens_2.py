class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return 1
        ans = 0
        permutation = [-1 for i in range(n)]
        col = [True for i in range(n)]
        diagonal = [True for i in range(2*n-1)]
        diagonal_reverse = [True for i in range(2*n-1)] 
        j = 0
        while not (j==0 and permutation[0]==n-1):
            need_bt = True
            for i in range(permutation[j]+1,n):
                if col[i] and diagonal[i+j] and diagonal_reverse[j-i]:
                    if permutation[j] != -1:
                        col[permutation[j]] = True  
                        diagonal[permutation[j]+j] = True
                        diagonal_reverse[j-permutation[j]] = True
                    permutation[j] = i
                    col[i] = False
                    diagonal[i+j] = False
                    diagonal_reverse[j-i] = False
                    j += 1
                    need_bt = False
                    break
            if j == n:
                ans += 1
                j = permutation[n-1]
                col[j] = True  
                diagonal[n-1+j] = True
                diagonal_reverse[n-1-j] = True 
                permutation[n-1] = -1
                j = n-2
            elif need_bt or permutation[j] == n-1:
            # back tracing
                if permutation[j] == -1:
                    j -= 1
                else:
                    col[permutation[j]] = True  
                    diagonal[permutation[j]+j] = True
                    diagonal_reverse[j-permutation[j]] = True 
                    permutation[j] = -1
                    j -= 1      
        return ans