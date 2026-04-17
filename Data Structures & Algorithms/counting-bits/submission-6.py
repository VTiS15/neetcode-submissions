class Solution:
    def countBits(self, n: int) -> List[int]:
        """Using bit_count() also results in O(n) time complexity.
        
        """
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == 2 * offset:
                offset = i
            dp[i] = dp[i - offset] + 1
        
        return dp
        