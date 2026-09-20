from collections import defaultdict 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            char[s[r]] += 1
            
            while (r - l + 1) - max(char.values()) > k:
                char[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res