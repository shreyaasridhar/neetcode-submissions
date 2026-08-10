class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        minVal, maxVal = 0 , len(nums) - 1
        mid = maxVal // 2
        if target > nums[maxVal]:
            return len(nums)
        if target < nums[minVal]:
            return 0
        while minVal < maxVal:
            print(minVal, maxVal, mid)
            if nums[mid] == target:
                return mid
            if target < nums[mid] and target > nums[mid-1]:
                return mid
            if nums[mid] < target:
                minVal = mid + 1
            else:
                maxVal = mid - 1
            mid = minVal + (maxVal - minVal) // 2
        return mid
        