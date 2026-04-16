from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amount: int):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            return min(dp(amount - coin) + 1 for coin in coins)

        res = dp(amount)
        if res > amount:
            return -1
        return res
        