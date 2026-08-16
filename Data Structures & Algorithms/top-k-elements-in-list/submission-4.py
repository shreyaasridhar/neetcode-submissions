from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = []
        for val, count in counts.items():
            arr.append([count, val])
        arr.sort()
        output = []
        while len(output) < k:
            output.append(arr.pop()[1])
        return output[:k]
