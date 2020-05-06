class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = [0]*(ord('z')-ord('A')+1)
        for c in J:
            jewels[ord(c)-ord('A')] = 1
        ans = 0
        for c in S:
            if jewels[ord(c)-ord('A')] == 1:
                ans += 1
        return ans


if __name__ == '__main__':
    ret = Solution().numJewelsInStones('aA', 'aAAbbbb')
    print(ret)
