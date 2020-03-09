class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        if dividend ^ divisor < 0:
            negetive_result = True
        else:
            negetive_result = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        max_power = 31
        result = 0
        while dividend >= divisor:
            for i in range(max_power,-1,-1):
                if (dividend >> i) >= divisor:
                    break
            max_power = i
            result += 1<<i
            dividend -= divisor << i
        if negetive_result:
            return -result
        else:
            return result
            
        
        
        # # This method is too slow
        # if dividend>0 and divisor>0 :
        #     i = -1
        #     while dividend >= 0:
        #         i += 1
        #         dividend -= divisor
        # elif dividend<0 and divisor<0 :
        #     if dividend == -2**31 and divisor == -1:
        #         return 2**31-1
        #     i = -1
        #     while dividend <= 0:
        #         i += 1
        #         dividend -= divisor
        # elif dividend>0 and divisor<0 :
        #     i = 1
        #     while dividend >= 0:
        #         i -= 1
        #         dividend += divisor
        # elif dividend<0 and divisor>0 :
        #     i = 1
        #     while dividend <= 0:
        #         i -= 1
        #         dividend += divisor
        # else:
        #     i = 0
        # return i
        