class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        pattern = [0] * 26
        for c in s1:
            pattern[ord(c) - ord('a')] += 1
        # print(pattern)
        l,r = 0, 0
        match = [0] * 26
        while r < len(s1):
            match[ord(s2[r]) - ord('a')] += 1
            r += 1
        if match == pattern:
            return True
        while r < len(s2):
            # print(s2[l],s2[r], match)
            match[ord(s2[l]) - ord('a')] -= 1
            match[ord(s2[r]) - ord('a')] += 1

            if match == pattern:
                return True
            l += 1
            r += 1

        return False
        