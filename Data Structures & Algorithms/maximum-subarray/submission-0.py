class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArray = nums[0]
        curSubArray = 0
        for n in nums:
            if curSubArray < 0:
                curSubArray = 0 
            curSubArray += n
            maxSubArray = max(maxSubArray, curSubArray)
        return maxSubArray