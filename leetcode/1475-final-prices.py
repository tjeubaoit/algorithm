from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, p in enumerate(prices):
            for j in range(i+1, len(prices)):
                if p >= prices[j]:
                    prices[i] -= prices[j]
                    break
        return prices


if __name__ == '__main__':
    prices = [8, 4, 6, 2, 3]
    ret = Solution().finalPrices(prices)
    print(ret)
