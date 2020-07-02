package sieunhan.algorithm.leetcode;

import java.util.Arrays;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class SquareSortedArray {

    private static int sqr(int n) {
        return (int) Math.pow(n, 2);
    }

    public int[] sortedSquares(int[] nums) {
        int i = 0;
        while (nums[i] < 0) i++;

        int j = i--, k = 0;
        int[] ans = new int[nums.length];
        // System.out.println(i + " " + j);

        while (i >= 0 && j < nums.length) {
            if (sqr(nums[i]) > sqr(nums[j])) {
                ans[k++] = sqr(nums[j]);
                j += 1;
            } else {
                ans[k++] = sqr(nums[i]);
                i -= 1;
            }
        }
        while (i >= 0)
            ans[k++] = sqr(nums[i--]);
        while (j < nums.length)
            ans[k++] = sqr(nums[j++]);

        return ans;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{-4, -1, 0, 3, 10};
        int[] ans = new SquareSortedArray().sortedSquares(nums);
        System.out.println(Arrays.toString(ans));
    }
}
