class Solution(object):
    def myAtoi(self, str_):
        """
        :type str: str
        :rtype: int
        """
        #find head
        if len(str_)==0: return 0
        valid_head = [" ","+","-"] + [str(i) for i in range(10)]
        for head in range(len(str_)):
            if str_[head] not in valid_head:
                return 0
            if str_[head] != " ":
                break
        #find tail
        valid_tail = [str(i) for i in range(10)]
        for tail in range(head+1,len(str_)):
            if str_[tail] not in valid_tail:
                if str_[head:tail] in ["+","-"]:
                    return 0
                return max(min(int(str_[head:tail]), 2**31-1), -2**31)
            if  tail == len(str_)-1:
                return max(min(int(str_[head:]), 2**31-1), -2**31)
        if str_[head:] in ["+","-"," "]:
            return 0
        return max(min(int(str_[head:]), 2**31-1), -2**31)
        
