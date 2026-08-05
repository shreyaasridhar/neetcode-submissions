class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        refDict = set()
        for x in nums:
            if(x in refDict):
                return True
            refDict.add(x)
        return False