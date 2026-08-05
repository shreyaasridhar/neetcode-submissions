class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap, tMap = {}, {}
        for i,j in zip(s,t):
            sMap[i] = sMap.get(i,0) + 1
            tMap[j] = tMap.get(j,0) + 1
        return sMap == tMap
