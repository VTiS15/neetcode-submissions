"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from operator import itemgetter


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        n = len(intervals)
        res = count = s = e = 0
        while s < n and e < n:
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        
        return res