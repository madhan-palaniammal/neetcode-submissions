class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        S = 0
        E = 1
        
        pos = len(intervals)
        for i, interval in enumerate(intervals):
            if interval[S] >= newInterval[S]:
                pos = i
                break

        intervals.insert(pos, newInterval)

        new_intervals = []
        new_intervals.append(intervals[0])
        prev = 0
        for i in range(1, len(intervals)):
            start = intervals[i][S]
            end = intervals[i][E]

            if start <= new_intervals[prev][E]:
                new_intervals[prev][E] = max(new_intervals[prev][E], end)
            else:
                new_intervals.append([start, end])
                prev += 1

        return new_intervals



        