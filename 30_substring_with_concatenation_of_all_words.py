class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s)==0 or len(words)==0:
            return []
        import copy
        ans = []
        words_map = {}
        for word in words:
            words_map[word] = 0
        for word in words:
            words_map[word] += 1
        word_len = len(words[0])
        ans_len = word_len * len(words)
        i = 0
        while i + ans_len <= len(s):
            candidate_map = copy.copy(words_map)
            fit = True
            for j in range(i,i+ans_len,word_len):
                if (s[j:j+word_len] in candidate_map.keys()) and (candidate_map[s[j:j+word_len]]>0):
                   candidate_map[s[j:j+word_len]] -= 1
                else:
                    fit = False
                    break
            if j == i + ans_len - word_len and fit and candidate_map[s[j:j+word_len]] == 0:
                ans.append(i)
            i += 1
        return ans


