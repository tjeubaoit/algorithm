class Solution {

    // O(N) solution
    public int arrangeCoins3(int n) {
        int c = 1;
        while(n>=c) {
            n-=c;
            c++;
        }
        return --c;

    // Math solution
    public int arrangeCoins2(int n) {
        long c = 2 * (long) n;
        double v = (-1 + Math.sqrt(1 + 4 * c)) / 2;
        return (int) Math.floor(v);
    }

    // O(NlogN) solution   
    public int arrangeCoins(int n) {
        long lo = 1, hi = n; int target = n;
        while (lo <= hi) {
            long m = lo + (hi-lo)/2;
            long value = m*(m+1)/2;
            if (value == target)
                return (int) m;
            else if (value > n) 
                hi = m - 1;
            else 
                lo = m + 1;
        }
        return (int)lo - 1;
    }
}