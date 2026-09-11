class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = [x.lower() for x in s if (x.isalnum())]
        second = first[::-1]
        return (first == second)
