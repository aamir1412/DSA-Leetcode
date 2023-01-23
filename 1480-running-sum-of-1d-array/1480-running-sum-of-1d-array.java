class Solution {

    public int[] runningSum(int[] nums) {
        int[] res = new int[nums.length];
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            res[i] = nums[i] + sum;
            sum = res[i];
        }
        return res;
    }
}
