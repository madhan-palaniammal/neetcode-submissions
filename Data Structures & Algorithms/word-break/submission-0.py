class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        words = set(wordDict)

        success_i = [len(s)]
        for i in range(len(s) - 1, -1 , -1):
            for last_sub_start in success_i:
                sub = s[i:last_sub_start]
                dp[i] = sub in words and dp[i+len(sub)]
                if dp[i]:
                    success_i.append(i)
                    break

        return dp[0]
                
