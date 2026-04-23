class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                if s[l] in count:
                    count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res