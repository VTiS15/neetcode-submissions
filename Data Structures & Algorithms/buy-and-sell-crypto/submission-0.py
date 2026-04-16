class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        sum_diff = 0
        for i in range(len(prices) - 1):
            sum_diff = max(0, sum_diff + prices[i + 1] - prices[i])
            res = max(res, sum_diff)
        
        return res
        