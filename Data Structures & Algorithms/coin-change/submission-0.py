class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(target):
            if target == 0:
                return 0

            if target in dp:
                return dp[target]

            min_coins = amount + 1
            for c in coins:
                if (target - c) >= 0:
                    min_coins = min(min_coins, dfs(target - c) + 1)
            
            dp[target] = min_coins

            return dp[target]

        min_coins = dfs(amount)
        return -1 if min_coins == amount + 1 else min_coins