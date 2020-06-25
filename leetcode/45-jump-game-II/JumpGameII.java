class JumpGameII {
    public int jump(int[] nums) {
        int[] steps = new int[nums.length];

        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] + i >= nums.length - 1) {
                steps[i] = 1;
                continue;
            }

            int minHere = Integer.MAX_VALUE;
            for (int j = nums[i]; j >= 1; --j) {
                int step = steps[i + j] + 1;
                if (step > 0 && step < minHere) {
                    minHere = step;
                }
            }
            steps[i] = minHere;
        }
        // System.out.println(Arrays.toString(steps));
        return steps[0];
    }
}