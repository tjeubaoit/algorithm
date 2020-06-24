from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]*len(arr)
        for i in range(len(arr)-2, -1, -1):
            ans[i] = max(ans[i+1], arr[i+1])
        return ans