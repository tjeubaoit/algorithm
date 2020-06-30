class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sums = [0]*(len(A)+1)
        for i in range(0, len(A)):
            sums[i+1] = (sums[i] + A[i]) % K
            
        count = collections.Counter(sums)
        return sum(v*(v-1)//2 for v in count.values())
