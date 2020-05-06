class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        lowest = prices[0]
        profit = 0
        for p in prices:
            profit = max(profit, p - lowest)
            lowest = min(lowest, p)
        return profit


if __name__ == '__main__':
    ret = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    # ret = Solution().maxProfit([7,6,4,3,1])
    print(ret)
