from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)

        def next_step(pos):
            return (pos + nums[pos] + n) % n

        for i in range(len(nums)):
            # Ignore visited number
            if nums[i] == 0: continue

            slow, fast = i, i
            direction = 1 if nums[i] > 0 else -1
            while True:
                slow = next_step(slow)
                pre_fast = next_step(fast)
                fast = next_step(pre_fast)
                # If cycle is not follow a single direction then break loop
                if nums[fast] * direction < 0 or nums[pre_fast] * direction < 0:
                    break
                if slow == fast:  # Cycle detected
                    # If cycle's length equals 1
                    if slow == next_step(slow):
                        break
                    return True
            slow = i
            # Mark numbers in current cycle as visited
            while nums[slow] * direction > 0:
                tmp = slow
                slow = next_step(slow)
                nums[tmp] = 0
        return False


if __name__ == '__main__':
    # nums = [2, -1, 1, 2, 2]
    # nums = [-1, 2]
    nums = [-2, 1, -1, -2, -2]
    # nums = [3, 1, 2]
    ret = Solution().circularArrayLoop(nums)
    print(ret)
