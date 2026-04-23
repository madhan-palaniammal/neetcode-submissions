class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        uniques = set(nums)
        starts = []
        for n in uniques:
            if n-1 not in uniques:
                starts.append(n)

        res = 1
        for s in starts:
            c = 1
            while s + c in uniques:
                c += 1
                
            res = max(res, c)

        return res