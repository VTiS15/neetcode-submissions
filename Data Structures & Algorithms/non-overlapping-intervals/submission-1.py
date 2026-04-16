from operator import itemgetter


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(1))
        res = 0
        prev = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                res += 1
            else:
                prev = i
        return res
        