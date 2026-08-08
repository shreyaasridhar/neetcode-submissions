class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSeen = {}
        for i in range(len(nums)):
            if target - nums[i] in numsSeen:
                return [numsSeen[target - nums[i]], i]
            numsSeen[nums[i]] = i