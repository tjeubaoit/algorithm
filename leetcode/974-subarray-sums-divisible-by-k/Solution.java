class Solution {
    public int subarraysDivByK(int[] A, int K) {
        // map from cumulative sum's modulo to its appear times
        int[] count = new int[K];
        count[0] = 1;
        int ans = 0, sum = 0;
        for (int x : A) {
            sum += x;
            // Redundant + K because in Java mod function 
            // may return negative value
            int idx = (sum % K + K) % K;
            ans += count[idx]++;
        }
        return ans;
    }
}