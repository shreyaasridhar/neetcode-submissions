class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (2*len(nums))
        for i, num in enumerate(nums):
            ans[i] = ans[i+len(nums)] = num
        return ans