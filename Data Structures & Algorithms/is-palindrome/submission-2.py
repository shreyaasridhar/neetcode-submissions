class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(filter(str.isalnum, s)).lower()
        x = t[::-1]
        return x == t
        
