class Solution:
    def climbStairs(self, n: int) -> int:
        if 1 <= n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[-2] = 1
        dp[-3] = 2
        for i in range(n - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]
        