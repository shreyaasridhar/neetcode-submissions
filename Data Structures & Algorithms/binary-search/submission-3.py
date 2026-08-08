class Solution:
    def search(self, nums: List[int], target: int) -> int:
        maxVal, minVal = len(nums) - 1, 0
        mid = (maxVal - minVal) // 2
        while minVal <= maxVal:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                maxVal = mid - 1
            else:
                minVal = mid + 1
            mid = minVal + (maxVal - minVal) // 2
            print(mid)
        return -1

        