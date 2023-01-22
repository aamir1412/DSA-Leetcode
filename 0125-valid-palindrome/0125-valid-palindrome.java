class Solution {

    public static boolean isAlphaNum(char ch) {
        // return (Character.isAlphabetic(ch) || Character.isDigit(ch));
        return Character.isLetterOrDigit(ch);
    }

    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            char l, r;
            l = s.charAt(i);
            r = s.charAt(j);
            if (isAlphaNum(l) == false) {
                i++;
                continue;
            }
            if (isAlphaNum(r) == false) {
                j--;
                continue;
            }
            
            l = Character.toLowerCase(l);
            r = Character.toLowerCase(r);
            if (Character.compare(l, r) != 0) {
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
}
