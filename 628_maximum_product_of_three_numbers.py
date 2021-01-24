class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        if len(nums) <= 3 :
            for i in nums:
                product *= i
            return product
        positive = []
        negative = []
        zero = []
        for i in nums:
            if  i > 0:
                positive.append(i)
            elif i < 0:
                negative.append(-i)
            else:
                zero.append(i)
        candidate_product = 0
        if len(positive) >=3:  #3p
            positive_top3 = []
            for j in range(3):
                max1 = max(positive)
                positive_top3.append(max1)
                positive[positive.index(max1)] = -1
            product = 1
            for i in positive_top3:
                product *= i
            candidate_product  = product
        if len(positive) >= 1 and len(negative) >= 2: #1p2n
            negative_top2 = []
            for j in range(2):
                max1 = max(negative)
                negative_top2.append(max1)
                negative[negative.index(max1)] = -1
            product = 1
            for i in negative_top2:
                product *= i
            if len(positive) >=3:
                product *= positive_top3[0]
                return max(candidate_product,product)
            else:
                return product*max(positive)
        elif candidate_product:
            return candidate_product
        
        if zero:
            return 0

        # max product can't be >=0, only the following two situation
        # 1. no positive 
        # 2. only one negative -> only 1n2p -> len=3,which we have dealed with at the  beginng
        # in general, if  the code  reach here, it means we only have negative 

        max_negative = max(negative) + 1
        negative_bottom3 = []
        for j in range(3):
            min1 = min(negative)
            negative_bottom3.append(min1)
            negative[negative.index(min1)] = max_negative
        candidate_product = 1
        for i in negative_bottom3:
            candidate_product *=  i
        return -candidate_product
        
        