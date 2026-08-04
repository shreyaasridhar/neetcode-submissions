class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sletters = {}
        tletters = {}
        for i in s:
            if i not in sletters:
                sletters[i] = 1
            curVal = sletters[i]
            sletters[i] = curVal + 1

        for i in t:
            if i not in tletters:
                tletters[i] = 1 
            curVal = tletters[i]
            tletters[i] = curVal + 1
        
        if len(tletters) != len(sletters): 
            return False
        anagramlen = len(sletters) if len(sletters) > len(tletters) else len(tletters)
        for i in sletters:
            if (i in tletters) and (sletters[i] == tletters[i]):
                anagramlen = anagramlen - 1
            else:
                return False
        
        return True if anagramlen == 0 else False
        