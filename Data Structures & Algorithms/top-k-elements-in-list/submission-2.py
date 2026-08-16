from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        countValueDict = defaultdict(list)
        for val, count in counts.items():
            countValueDict[count].append(val)
        output = []
        while len(output) < k:
            maxVal = max(countValueDict.keys())
            output += countValueDict[maxVal]
            countValueDict.pop(maxVal)
        return output[:k]
