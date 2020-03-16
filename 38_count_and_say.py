class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        write = "11"
        for i in range(n-2):
            read = ""
            count = 0
            for j in range(1,len(write)):
                if write[j] != write[j-1]:
                    read += str((j-count)) + write[j-1]
                    count = j
            read += str((j-count+1)) + write[j] 
            write = read
        return write

solution = Solution()
print(solution.countAndSay(4))