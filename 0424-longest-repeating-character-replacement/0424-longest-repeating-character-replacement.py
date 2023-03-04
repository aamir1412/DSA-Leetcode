class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxx = 0
        maxfq = 0
        dct = {}
        l, r = 0, 0
        while r < len(s):
            dct[s[r]] = 1 + dct.get(s[r], 0)
            maxfq = max(maxfq, dct[s[r]])
            wnd = r - l + 1
            if wnd - maxfq <= k:
                maxx = max(maxx, wnd)
            else:
                dct[s[l]] -= 1
                l += 1
            r += 1
        return maxx