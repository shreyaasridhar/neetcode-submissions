class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictOfNums = {}
        output = []
        for i, num in enumerate(nums):
            dictOfNums[num] = dictOfNums.get(num, 0) + 1

        sorted_keys = sorted(dictOfNums, key=lambda k: dictOfNums[k], reverse=True)

        return sorted_keys[:k]