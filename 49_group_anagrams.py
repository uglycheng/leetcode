class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # # the most ordinary method
        # groups = {}
        # for string in strs:
        #     # key = list(string)
        #     # key.sort()
        #     # key = "".join(key)
        #     key = "".join(sorted(string))
        #     if key in groups.keys():
        #         groups[key].append(string)
        #     else:
        #         groups[key] = [string]
        # return list(groups.values())
        
        # # this method cannot handle the situation when there are duplicate characters in string , for example, "huh","tit" has the same index
        # beginning = ord("a")
        # groups = {}
        # for string in strs:
        #     index = 0
        #     for char in string:
        #         index += 1 << (ord(char)-beginning)
        #     if index in groups.keys():
        #         groups[index].append(string)
        #     else:
        #         groups[index] = [string]
        # return list(groups.values())

        # last solution we use the binary number to represent the string, the limitation is it cannot distinguish "huh",  "tit"
        # this time we can use a string in the format of #0#1#..........#3#0, this way we can save space comparing to using a list[0,1,...3,0]        
        beginning = ord("a")
        groups = {}
        for string in strs:
            count = [0 for i in range(26)]
            for char in string:
                count[ord(char)-beginning] += 1
            key = ""
            for i in range(26):
                key += "#"+str(count[i])
            if key in groups.keys():
                groups[key].append(string)
            else:
                groups[key] = [string]
        return list(groups.values())
        
        # another solution is to use the first 26 prime numbers to represent 26 characters, and use their product to represent the string
        # in this way the representation is unique for diffenrent groups but the problem is it may cost too much space when you meet strings like "zzzzzzzzzzzzzzzzzzzzzzzzzzzzz"