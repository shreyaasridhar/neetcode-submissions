class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIndex = {}
        diffsIndex = {}
        res = []
        for i in range(len(nums)):
            numsIndex[nums[i]] = i
            diffsIndex[i] = target - nums[i]
        print(numsIndex, diffsIndex)

        for key, value in diffsIndex.items():
            if value in nums and numsIndex.get(value) != key:
                res = [key, numsIndex[value]]
                print(res)
                return res