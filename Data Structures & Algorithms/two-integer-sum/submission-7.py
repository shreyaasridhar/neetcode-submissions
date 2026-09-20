class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSeen = {}
        for i, num in enumerate(nums):
            if target - num in numsSeen:
                return [numsSeen[target - num], i]
            numsSeen[num] = i