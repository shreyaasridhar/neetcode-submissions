class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_hash = {}
        value_index = {}
        for i in range(len(nums)):
            value_index[nums[i]] = i
        for i in range(len(nums)):
            complement_hash[i] = target - nums[i]
        print(complement_hash)
        print(value_index)
        for key, value in complement_hash.items():
            if value in value_index:
                if value_index.get(value) != key:
                    return [key,value_index[value]]