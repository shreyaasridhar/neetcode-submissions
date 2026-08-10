class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mini, maxi = 0, len(nums) - 1
        i = maxi // 2

        while(maxi >= i and mini <= maxi):
            if nums[i] == target:
                return i
            if nums[i] < target:
                mini = i + 1
            elif nums[i] > target:
                maxi = i - 1

            i = (maxi - mini) // 2 + mini

        if mini - maxi == 1:
            return mini
        