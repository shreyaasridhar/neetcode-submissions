class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniquedict = defaultdict(list)

        for i in strs:
            uniquedict["".join(sorted(i))].append(i)
        
        res = []

        for key, value in uniquedict.items():
            res.append(value)

        return res