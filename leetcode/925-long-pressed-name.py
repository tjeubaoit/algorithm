class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        return self.twoPointersSolution(name, typed)

    def twoPointersSolution(self, name, typed):
        j = 0
        for i in range(len(name)):
            if j == len(typed):
                return False
            if name[i] != typed[j]:
                if i == 0:
                    return False
                # Discard remain same values
                while j < len(typed) and typed[j] == name[i-1]:
                    j += 1
                if j == len(typed) or typed[j] != name[i]:
                    return False
            j += 1
        for i in range(j, len(typed)-1):
            if typed[i] != typed[i+1]:
                return False
        return True

    # Could not pass latest test cases
    def groupSolution(self, name: str, typed: str) -> bool:
        def groupify(s):
            groups = []
            i = 0
            for j in range(1, len(s)):
                if s[j] != s[i]:
                    groups.append((s[i], j-i))
                    i = j
            if i < len(s):
                groups.append((s[i], len(s)-i))
            return groups

        gname = groupify(name)
        gtyped = groupify(typed)
        if len(gname) != len(gtyped):
            return False

        for i in range(len(gname)):
            if gname[i][0] != gtyped[i][0] or gname[i][1] > gtyped[i][1]:
                return False
        return True


if __name__ == '__main__':
    name = "zlexya"
    typed = "aazlllllllllllllleexxxxxxxxxxxxxxxya"
    print(Solution().isLongPressedName(name, typed))
