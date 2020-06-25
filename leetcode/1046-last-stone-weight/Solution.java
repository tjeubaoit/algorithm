class Solution {
    public int lastStoneWeight(int[] stones) {
        int[] counts = new int[1001];
        for (int stone : stones) {
            counts[stone] += 1;
        }
        int i = 1000;
        while (i > 0) {
            if (counts[i] == 0) {
                i--;
                continue;
            }
            if (counts[i] > 1) counts[i] = counts[i] % 2;
            if (counts[i] > 0) {
                int j = i - 1;
                while (j > 0 && counts[j] == 0) j--;
                if (j <= 0) return i;
                counts[i] = 0;
                counts[j] -= 1;
                counts[i-j] += 1;
            }
            i--;
        }
        return counts[1];
    }
}