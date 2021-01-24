def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        xor_without_last = 0
        for i in range(0,len(encoded),2):
            xor_without_last = xor_without_last ^ encoded[i]
        # 1 to n xor :  n%4: {1:1,2:n+1,3:0, 0:n}
        j = (len(encoded)+1) % 4
        if j== 1:
            xor_all = 1
        elif j== 2:
            xor_all = len(encoded)+1+1
        elif j== 3:
            xor_all = 0
        elif j== 0:
            xor_all = len(encoded)+1
        last_one = xor_all ^ xor_without_last
        encoded.append(last_one)
        for i in  range(len(encoded)-1):
            encoded[-i-2] = encoded[-i-1] ^ encoded[-i-2]
        return encoded

        # warning don't use list.insert(),it's slow