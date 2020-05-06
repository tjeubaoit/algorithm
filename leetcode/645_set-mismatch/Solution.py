class Solution:

    def findErrorNums(self, nums):
        return self.solution2(nums)

    def solution1(self, nums):
        """
        Use XOR approach
        """
        pass

    def solution2(self, nums):
        """
        Use extra array/hash map approach
        """
        ct = [0] * len(nums)
        for num in nums:
            ct[num - 1] += 1
        dup, missing = -1, -1
        for i in range(0, len(nums)):
            if ct[i] == 2:
                dup = i + 1
            elif ct[i] == 0:
                missing = i + 1
        return [dup, missing]

    def solution3(self, nums):
        """
        Use O(1) space
        """
        dup, missing = -1, -1
        for n in nums:
            if nums[abs(n)-1] < 0:
                dup = abs(n)
            else:
                nums[abs(n)-1] *= -1
        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]


if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    ret = Solution().solution3(nums)
    print(ret)
