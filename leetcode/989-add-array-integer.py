from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        if K == 0:
            return A
        if len(A) < 6:
            A = [0]*(6-len(A)) + A
        i = len(A) - 1
        d = 0
        while i >= 0 and (d > 0 or K > 0):
            x = K % 10
            K //= 10
            s = A[i] + x + d
            if s >= 10:
                d = 1
                A[i] = s - 10
            else:
                d = 0
                A[i] = s
            i -= 1
        if d > 0:
            A = [1] + A
        i = 0
        while i < len(A):
            if A[i] != 0: break
            i += 1
        return A[i:]
