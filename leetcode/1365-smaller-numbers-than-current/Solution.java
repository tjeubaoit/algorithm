import java.util.Arrays;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class LeetCode1365 {

    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] counts = new int[102];
        for (int n : nums) {
            counts[n+1] += 1;
        }
        for (int i = 1; i < counts.length; i++) {
            counts[i] = counts[i-1] + counts[i];
        }

        int[] ans = new int[nums.length];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = counts[nums[i]];
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new LeetCode1365().smallerNumbersThanCurrent(
//                new int[]{8,1,2,2,3}
//                new int[]{6,5,4,8}
                new int[]{5,0,10,0,10,6}
        )));
    }
}
