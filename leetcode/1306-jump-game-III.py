from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        st = [start]
        while st:
            i = st.pop()
            fw = i + arr[i]
            bw = i - arr[i]
            if fw < len(arr):
                if arr[fw] == 0:
                    return True
                elif fw not in visited:
                    st.append(fw)
                    visited.add(fw)
            if bw >= 0:
                if arr[bw] == 0:
                    return True
                elif bw not in visited:
                    st.append(bw)
                    visited.add(bw)
        return False
