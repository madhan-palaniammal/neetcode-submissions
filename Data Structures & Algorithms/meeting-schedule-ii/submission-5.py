"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        meetings = []

        for interval in intervals:
            if meetings and meetings[0] <= interval.start:
                heapq.heappop(meetings)

            heapq.heappush(meetings, interval.end)

        return len(meetings)