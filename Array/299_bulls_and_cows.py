class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        
        nums = [0 for i in range(10)]
        for i in range(len(secret)):
            nums[int(secret[i])] += 1
        
        A = 0
        for i in range(len(secret)):
            if guess[i] ==  secret[i]:
                A += 1
                nums[int(secret[i])] -= 1

        B = 0
        for i in range(len(guess)):
            if nums[int(guess[i])]>0 and guess[i] !=  secret[i]:
                B += 1
                nums[int(guess[i])] -= 1
        
        return str(A)+"A"+str(B)+"B"

        # a very clever solution
