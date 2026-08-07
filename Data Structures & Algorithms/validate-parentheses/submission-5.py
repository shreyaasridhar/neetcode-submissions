class Solution:
    def isValid(self, s: str) -> bool:
        myArr, i= [], 0
        print("len(s)-> ", len(s))
        myHash ={ ")" : "(", "}" :"{", "]": "[" }
        while i < len(s):
            if s[i] in "({[":
                myArr.append(s[i])
            else:
                if len(myArr) == 0:
                    return False
                if myHash[s[i]] != myArr[-1]:
                    return False
                myArr.pop()
            i += 1
        if len(myArr) != 0:
            return False
        return True