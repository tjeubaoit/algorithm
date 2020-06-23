from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals = sorted(intervals)
        ans = []
        it = intervals[0]
        for i in range(1, len(intervals)):
            if it[1] >= intervals[i][0]:
                it = [it[0], max(it[1], intervals[i][1])]
            else:
                ans.append(it)
                it = intervals[i]
        ans.append(it)
        return ans

    # Better solution
    # Keep current iterator in last element of merged array instead of 'it' variable
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(arr))
