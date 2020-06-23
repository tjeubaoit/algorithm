class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        return self.groupSolution(name, typed)

    def twoPointersSolution(self, name, typed):
        pass

    def groupSolution(self, name: str, typed: str) -> bool:
        if not name and not typed:
            return True
        if not name or not typed:
            return False

        cname = self.compress(name)
        ctyped = self.compress(typed)
        if len(cname) != len(ctyped):
            return False
        # print(cname)
        # print(ctyped)

        for i in range(0, len(cname)):
            s1, c1 = cname[i]
            s2, c2 = ctyped[i]
            if s1 != s2 or c1 > c2:
                return False

        return True

    def compress(self, strs):
        s1 = []
        last = strs[0]
        count = 0
        for c in strs:
            if c != last:
                s1.append((last, count))
                last = c
                count = 1
            else:
                count += 1
        return s1
