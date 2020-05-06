class Solution:
    def maxProfit(self, prices):
        return self.solution(prices)

    def solution(self, prices):
        if not prices:
            return 0
        max_profit = 0
        lowest = prices[0]
        curr = 0
        for i in range(1, len(prices)):
            highest = prices[i]
            if highest - lowest > curr:
                curr = highest - lowest
            else:
                lowest = highest
                max_profit += curr
                curr = 0
            # print(lowest, highest, curr)
        return max_profit + curr

    def betterSolution(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
