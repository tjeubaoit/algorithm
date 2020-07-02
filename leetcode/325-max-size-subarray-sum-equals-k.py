class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        d = {0: -1}
        ans, total = 0, 0
        for i, n in enumerate(nums):
            total += n
            if total-k in d:
                ans = max(ans, i - d[total-k])
            if total not in d:
                d[total] = i
        return ans


if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    ret = Solution().maxSubArrayLen(nums, k=3)
    print(ret)
