class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberMap = {}
        for i in nums:
            if i in numberMap:
                return True
            numberMap[i] = True
        return False
