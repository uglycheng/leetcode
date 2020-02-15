class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        zigzag_matrix = [""] * numRows
        row = 0
        change_of_row = 1
        for char in s:
            zigzag_matrix[row] += char
            row += change_of_row
            if row==0 or row==(numRows-1):
                change_of_row *= -1
        return "".join(zigzag_matrix)

        
        # #Below is my original solution
        # if len(s)==0 or numRows==1:
        #     return s
        # index_in_series = 0
        # num_chars_in_one_series = 2 * numRows - 2
        # half_num_chars_in_one_series = num_chars_in_one_series / 2
        # row  = 0
        # zigzag_matrix = [s[0]] + ["" for i in range(numRows-1)]
        
        # # This block tries to use if-else to avoid mod opration, however I found conditional operation is slower than mod
        # # for char in s[1:]:
        # #     #this if-else avoid mod and divide 
        # #     if index_in_series == num_chars_in_one_series:
        # #         index_in_series = 1
        # #     else:
        # #         index_in_series += 1
        # #     #this if-else avoid mod and divide
        # #     if index_in_series > half_num_chars_in_one_series:
        # #         row -= 1
        # #     else:
        # #         row += 1
        # #     zigzag_matrix[row] += char
        
        # for j in range(1,len(s)):
        #     index_in_series = j % num_chars_in_one_series
        #     print(index_in_series)
        #     if index_in_series > half_num_chars_in_one_series or index_in_series==0:
        #         row -= 1
        #     else:
        #         row += 1
        #     print(row)
        #     print("\n")
        #     zigzag_matrix[row] += s[j]
        
        # return "".join(zigzag_matrix)

        

solution = Solution()
print(solution.convert("PAYPALISHIRING",3))
