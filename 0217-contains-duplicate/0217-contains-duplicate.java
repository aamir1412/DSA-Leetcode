class Solution {

    public boolean containsDuplicate(int[] nums) {
        Set<Integer> myset = new HashSet<Integer>();

        for (int i : nums) {
            if (myset.contains(i)) {
                return true;
            } else {
                myset.add(i);
            }
        }

        return false;
    }
}
