def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        max_ = len(languages)
        i = 0
        # preprocess:  this step is very important, at first I put this if line at pos 1,  and it exceeds time limits
        #              this is beacuse, you check if they need teach every i*j node, and many works are  duplicated
        while i < len(friendships):
            if set(languages[friendships[i][0]-1]) & set(languages[friendships[i][1]-1]) != set([]):
                del(friendships[i])
            else:
                i += 1
        for i in range(1,n+1):
            teach = [0 for j in range(len(languages))]
            for j in friendships:
                #  pos 1
                if (not teach[j[0]-1]) and (i not in languages[j[0]-1]):
                        teach[j[0]-1] = 1
                if (not teach[j[1]-1]) and (i not in languages[j[1]-1]):
                        teach[j[1]-1] = 1
            max_ = min(max_,sum(teach))
        return max_