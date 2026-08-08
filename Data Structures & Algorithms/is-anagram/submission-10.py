class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        sdict = {}
        tdict = {}

        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = 0
            sdict[s[i]] += 1

            if t[i] not in tdict:
                tdict[t[i]] = 0
            tdict[t[i]] += 1

        return sdict == tdict