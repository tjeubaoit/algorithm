package sieunhan.algorithm.leetcode;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class ReverseInteger {

    public int reverse(int x) {
        if (x == Integer.MIN_VALUE) return 0;
        int xAbs = Math.abs(x);

        long rev = 0;
        while (xAbs > 0) {
            int val = xAbs % 10;
            rev = rev * 10 + val;
            if (rev > Integer.MAX_VALUE) return 0;
            xAbs /= 10;
        }
        int n = (int) rev;
        return x > 0 ? n : -n;
    }

    public static void main(String[] args) {
        System.out.println(new ReverseInteger().reverse(-2147483412));
    }
}
