from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniqueDict = defaultdict(list)
        for i,s in enumerate(strs):
            counter = [0] * 26
            for x in s:
                counter[ord(x) - ord('a')] += 1
            uniqueDict[str(counter)].append(s)
        output = []
        for key, value in uniqueDict.items():
            output.append(value)
        return output
            
        # ["act","pots","tops","cat","stop","hat"]
        # sorted letter of each string as key
        # {
        #     [1,0,1,....] : ['act' , 'tac']
        #     'opst' : ['tops', 'stop']
        # }
        # "".join(sorted(s))
        # act