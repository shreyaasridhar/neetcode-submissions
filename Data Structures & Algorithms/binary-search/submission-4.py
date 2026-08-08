class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mini, maxi = 0, len(nums) - 1
        index = maxi // 2
        while(maxi >= index and mini <= index):
            if nums[index] == target:
                return index
            if nums[index] < target:
                mini = index + 1
            else:
                maxi = index - 1
            index = (maxi - mini) // 2 + mini
        
        return -1