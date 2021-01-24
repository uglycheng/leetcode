



def minCharacters(a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        a_count = [0 for i in range(26)]
        b_count = [0 for i in range(26)]
        for i in a:
            a_count[ord(i)-ord('a')]  += 1
        for i in b:
            b_count[ord(i)-ord('a')]  += 1
        
        # move a forward
        a_move  = len(a)
        b_move  = 0
        min_move = len(a)+len(b)
        for i in range(25):
            a_move -= a_count[i]
            b_move += b_count[i]
            min_move =  min(a_move+b_move,min_move)
        # move a backward
        b_move  = len(b)
        a_move  = 0
        for i in range(25):
            b_move -= b_count[i]
            a_move += a_count[i]
            min_move =  min(a_move+b_move,min_move)
        # change_both_a_b_consist only one distinct letter
        min_move = min(min_move,len(a)-max(a_count)+len(b)-max(b_count))
        return min_move

print(minCharacters('dabadd','cda'))