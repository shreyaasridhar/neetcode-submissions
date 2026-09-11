from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniqueDict = defaultdict(list)
        for i,s in enumerate(strs):
            uniqueDict["".join(sorted(s))].append(s)
        output = []
        for key, value in uniqueDict.items():
            output.append(value)
        return output
            


        # ["act","pots","tops","cat","stop","hat"]
        # sorted letter of each string as key
        # {
        #     'act' : ['act' , 'tac']
        #     'opst' : ['tops', 'stop']
        # }
        # "".join(sorted(s))
        # act