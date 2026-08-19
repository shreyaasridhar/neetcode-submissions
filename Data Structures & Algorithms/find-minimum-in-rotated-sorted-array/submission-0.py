class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l<r:
            mid = (l+r) // 2
            if nums[mid] > nums[l]:
                l = mid
            if nums[mid] < nums[r]:
                r = mid
            if nums[l]>nums[r] and l+1==r:
                return nums[r]
        return nums[r]