class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        dup = set()
        maxx = 0
        while r < len(s):
            if s[r] not in dup:
                dup.add(s[r])
                maxx = max(maxx, r - l + 1)
                r += 1
            else:
                l += 1
                dup.remove(s[l-1])            
        return maxx
                