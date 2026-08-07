class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHashSet = set(nums) 
        return len(myHashSet) != len(nums)