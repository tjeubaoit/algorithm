class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.solution1(nums, k)

    def solution1(self, nums, k):
        """
        Cyclic Replacements solution
        """
        n = len(nums)
        k %= n
        if k == 0: return

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1

    def solution2(self, nums, k):
        """
        Reverse solution

        This approach is based on the fact that when we rotate the array k times,
        k%nk elements from the back end of the array come to the front and the rest
        of the elements from the front shift backwards.

        In this approach, we firstly reverse all the elements of the array.
        Then, reversing the first k elements followed by reversing the rest
        n-kn−k elements gives us the required result.
        """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


if __name__ == '__main__':
    nums = [i + 1 for i in range(0, 6)]
    Solution().rotate(nums, 3)
    print(nums)
