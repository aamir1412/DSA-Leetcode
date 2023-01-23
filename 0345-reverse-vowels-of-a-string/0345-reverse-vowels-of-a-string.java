class Solution {

    public String reverseVowels(String s) {
        Set<Character> vow = new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        char[] res = s.toCharArray();
        char ch;

        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            if (vow.contains(res[l]) && vow.contains(res[r])) {
                ch = res[l];
                res[l] = res[r];
                res[r] = ch;
                l++;
                r--;
            }
            if (vow.contains(res[l]) == false) {
                l++;
            }
            if (vow.contains(res[r]) == false) {
                r--;
            }
        }
        String ans = new String(res);
        return ans;
    }
}
