class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = 0
        end = 1

        intervals.sort(key=lambda x: x[start])

        res = []
        prev = intervals[0]
        for interval in intervals:
            if prev[end] < interval[start]:
                res.append(prev)
                prev = interval
            else:
                prev[end] = max(prev[end], interval[end])

        res.append(prev)

        return res