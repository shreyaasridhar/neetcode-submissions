class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = set()
        maxLength, L = 0, 0

        for i in range(len(s)):

            while s[i] in charDict:
                charDict.remove(s[L])
                L += 1
            
            charDict.add(s[i])
            maxLength = max(maxLength, i - L + 1)

        return maxLength