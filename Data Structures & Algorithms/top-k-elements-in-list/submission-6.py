from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        for val, count in counts.items():
            arr[count].append(val)
        output = []
        for i in range(len(arr) - 1, 0, -1):
            if len(output) > k:
                break
            output += arr[i]
        
        return output[:k]
