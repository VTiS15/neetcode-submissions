from bisect import insort


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insort(intervals, newInterval)
        
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                merged = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]
                intervals.pop(i)
                intervals.pop(i)
                insort(intervals, merged)
            else:
                i += 1
        
        return intervals

        