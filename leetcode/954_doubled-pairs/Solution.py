from collections import Counter

class Solution(object):
    def canReorderDoubled(self, A):
        ct = collections.Counter(A)
        for k in sorted(ct, key=abs):
            if not ct[k]: continue
            if ct[2 * k] < ct[k]: return False
            ct[2*k] -= ct[k]
        return True



if __name__ == '__main__':
    import sys
    sl = Solution()
    sl.canReorderDoubled([int(i) for i in sys.argv[1].split(',')])
