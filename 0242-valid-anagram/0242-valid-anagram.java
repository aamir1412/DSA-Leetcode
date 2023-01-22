class Solution {

    public static Map<Character, Integer> getmap(String s) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            map.putIfAbsent(ch, 0);
            map.put(ch, map.get(ch) + 1);
        }
        return map;
    }

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> map_s = getmap(s);
        Map<Character, Integer> map_t = getmap(t);
        return map_t.equals(map_s);
    }
}
