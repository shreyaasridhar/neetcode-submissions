class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pDict = { ')':'(',']':'[','}':'{'}
        for i in s:
            if i in pDict.values():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if pDict[i] != stack.pop():
                    return False
        return False if len(stack) != 0 else True
            
