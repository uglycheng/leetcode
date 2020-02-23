class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #This solution cost longer time than the enumration solution which enumrates 'I','IV','IX' ... but is easier to generalize to situations with more symbols
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1, 5, 10, 50, 100, 500, 1000]
        roman = ""
        i = -1
        j = 2
        while num > 3 :
            roman += symbols[i] * (num//values[i])
            num = num % values[i]
            roman += (symbols[i-j] + symbols[i]) * (num//(values[i]-values[i-j]))
            num = num % (values[i]-values[i-j])  
            i -= 1
            if j==2 :
                j = 1
            else:
                j = 2
        roman += num * symbols[0]
        return roman