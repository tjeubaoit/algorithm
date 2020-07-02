package sieunhan.algorithm.leetcode;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class ArrangeCoins {

    public long arrangeCoins(int n) {
        int lo = 1, hi = n;
        while (lo <= hi) {
            int m = lo + (hi - lo) / 2;
            int s = m * (m + 1) / 2;
            if (n == s) return m;
            else if (n - s < 0) hi = m - 1;
            else lo = m + 1;
        }
        return lo - 1;
    }

    public long arrangeCoins2(int n) {
        long c = 2 * (long) n;
        double v = (-1 + Math.sqrt(1 + 4 * c)) / 2;
        return (int) Math.floor(v);
    }

    public static void main(String[] args) {
        System.out.println(new ArrangeCoins().arrangeCoins(1804289383));
        System.out.println(new ArrangeCoins().arrangeCoins2(1804289383));
    }
}
