class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] ct = new int[1001];
        for (int n : arr1) {
            ct[n] += 1;
        }
        int idx = 0;
        for (int n : arr2) {
            while (ct[n] > 0) {
                arr1[idx++] = n;
                ct[n] -= 1;
            }
        }
        for (int i = 0; i < 1001; i++) {
            while (ct[i] > 0) {
                arr1[idx++] = i;
                ct[i] -= 1;
            }
        }
        return arr1;
    }
}