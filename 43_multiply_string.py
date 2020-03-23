class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = 0
        for i in range(len(num1)):
            value1 = int(num1[i])
            temp = 0
            for j in range(len(num2)):
                temp += value1 * int(num2[j])
                temp *= 10
            ans += temp/10
            ans *= 10
        ans /= 10
        return str(ans)