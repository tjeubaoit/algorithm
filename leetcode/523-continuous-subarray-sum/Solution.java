import java.util.*;

class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int sum = 0;
        Map<Integer, Integer> ct = new HashMap<>();
        ct.put(0, 0);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            int mod = k != 0 ? sum%k : sum;
            if (!ct.containsKey(mod)) 
                ct.put(mod, i + 1);
            else if (i + 1 - ct.get(mod) >= 2)
                return true;
        }
        return false;
    }
}