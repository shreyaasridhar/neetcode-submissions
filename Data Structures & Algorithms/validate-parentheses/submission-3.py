class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pDict = { ')':'(',']':'[','}':'{'}
        for char in s:
            if char in pDict:
                if not stack or pDict[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
            
