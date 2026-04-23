"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [(0,40),(5,10),(15,20), (40, 80), (40, 60), (60, 80)]


        intervals.sort(key=lambda x: x.start)
        sol =0
        for i in range(len(intervals)):
            if not intervals[i]:
                continue

            end = intervals[i].end
            for j in range(i+1, len(intervals)):
                if not intervals[j]:
                    continue
                if end <= intervals[j].start:
                    end = intervals[j].end
                    intervals[j] = None

            sol +=1

        return sol
