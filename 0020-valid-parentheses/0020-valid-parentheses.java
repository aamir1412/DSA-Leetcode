class Solution {

    public boolean isValid(String s) {
        Stack<Character> st = new Stack<Character>();
        st.push('$');
        char[] c = s.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            if (c[i] == '(' || c[i] == '{' || c[i] == '[') {
                st.push(c[i]);
                continue;
            }

            if (c[i] == ')' && st.peek() == '(') {
                st.pop();
            } else if (c[i] == '}' && st.peek() == '{') {
                st.pop();
            } else if (c[i] == ']' && st.peek() == '[') {
                st.pop();
            } else {
                return false;
            }
        }

        if (st.peek() == '$') {
            return true;
        } else {
            return false;
        }
    }
}
