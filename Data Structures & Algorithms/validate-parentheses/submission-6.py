class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        myArr= []
        myHash ={ ")" : "(", "}" :"{", "]": "[" }
        for i in s:
            if i in "({[":
                myArr.append(i)
            else:
                if not myArr or myHash[i] != myArr[-1]:
                    return False
                myArr.pop()
        return not myArr