from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniqueDict = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for x in s:
                counter[ord(x) - ord('a')] += 1
            uniqueDict[str(counter)].append(s)
        return list(uniqueDict.values())
            
        # ["act","pots","tops","cat","stop","hat"]
        # sorted letter of each string as key
        # {
        #     [1,0,1,....] : ['act' , 'tac']
        #     'opst' : ['tops', 'stop']
        # }
        # "".join(sorted(s))
        # act