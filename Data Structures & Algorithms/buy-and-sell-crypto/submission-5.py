class Solution:   
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smaller = prices[0]
        for j in prices[1:]:
            if smaller > j:
                smaller = j
            profit = max(j-smaller,profit)
        return profit