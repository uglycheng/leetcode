class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        if newInterval[0] < intervals[0][0]:
            if newInterval[1] < intervals[0][0]:
                intervals.insert(0,newInterval)
            else:
                intervals[0][0] = newInterval[0]
                intervals[0][1] = max(newInterval[1],intervals[0][1])
        j = 0
        for j in range(1,len(intervals)):
            if intervals[j][0] > newInterval[0]:
                if intervals[j-1][1] < newInterval[0]:
                    intervals.insert(j,newInterval)
                    j += 1
                else:
                    intervals[j-1][1] = max(intervals[j-1][1],newInterval[1])
                j = -j
                break
        if j>=0 :
            if intervals[j][1] < newInterval[0]:
                intervals.append(newInterval)
            else:
                intervals[j][1] = max(intervals[j][1],newInterval[1]) 
            return intervals
        else:
            j = -j
        while j<len(intervals):
            if intervals[j-1][1] < intervals[j][0]:
                j += 1
            else:
                intervals[j-1][1] = max(intervals[j-1][1],intervals[j][1])
                del(intervals[j])
        return intervals
