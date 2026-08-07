class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHashSet = set(nums)
        return not (len(myHashSet) == len(nums))