class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        uniques = set()

        res = 0
        for c in s:
            if c not in uniques:
                uniques.add(c)
                q.append(c)
                res = max(res, len(q))
            else:
                while q and c in uniques:
                    x = q.popleft()
                    uniques.remove(x)
                
                uniques.add(c)
                q.append(c)
                res = max(res, len(q))
        
        return res
