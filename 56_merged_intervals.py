class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return intervals
        sort_intervals = {}
        i = 0
        while i < len(intervals):
            if intervals[i][0] in sort_intervals.keys():
                intervals[sort_intervals[intervals[i][0]]][1] = max(intervals[sort_intervals[intervals[i][0]]][1],intervals[i][1])
                del(intervals[i])
            else:
                sort_intervals[intervals[i][0]] = i
                i += 1
        order = list(sort_intervals.keys())
        order.sort()
        for i in range(len(order)):
            order[i] = sort_intervals[order[i]]
        sort_intervals = [intervals[order[0]]]
        for i in order[1:]:
            if intervals[i][0] <= sort_intervals[-1][1]:
                sort_intervals[-1][1] = max(intervals[i][1],sort_intervals[-1][1])
            else:
                sort_intervals.append(intervals[i])
        return sort_intervals

