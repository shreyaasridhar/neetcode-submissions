class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        maxlen = 0
        if not s:
            return maxlen
        seen = set()
        while l < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            maxlen = max(maxlen, (r-l))
            # print(l, r, seen, s[l], maxlen)
            seen.remove(s[l])
            l += 1
        return maxlen
            