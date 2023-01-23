class Solution {

    public int maximumWealth(int[][] accounts) {
        int maxx = 0;
        for (int[] i : accounts) {
            int sum = 0;
            for (int j : i) {
                sum = sum + j;
            }
            if (sum > maxx) {
                maxx = sum;
            }
        }

        return maxx;
    }
}
