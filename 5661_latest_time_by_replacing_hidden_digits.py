def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = time.split(':')
        h  = list(time[0])
        m  = list(time[1])
        if h[0] ==  '?':
            if ord('4')<=ord(h[1])<=ord('9'):
                h[0] = '1'
            else:
                h[0] = '2'
        if h[1] == '?':
            if h[0] == '2':
                h[1] = '3'
            else:
                h[1] = '9'
        h = h[0] +  h[1]
        if m[0] == '?':
            m[0] = '5'
        if m[1]  == '?':
            m[1] = '9'
        m = m[0] +  m[1]
        return ':'.join([h,m])