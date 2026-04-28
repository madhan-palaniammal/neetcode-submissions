class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for s in strs:
            key = tuple(sorted(s))
            result[key] = result.get(key, [])
            result[key].append(s)

        return list(result.values())