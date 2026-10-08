class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #  f       p
        # [5,2,3,1,4]
        # [2,3,1,4,5]
        # element at (n - k) when it is sorted 5 - 2 - this will be the second largest value so we can return it as is

        def partition(left, right, nums):
            pivot, fill = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[fill], nums[i] = nums[i], nums[fill]
                    fill += 1
            nums[fill], nums[right] = nums[right], nums[fill]
            return fill
        
        n, l, r = len(nums), 0, len(nums) - 1
        while l < r:
            pivot = partition(l, r, nums)
            if pivot < n - k:
                l = pivot + 1
            elif pivot > n - k:
                r = pivot - 1
            else:
                break
        return nums[n - k]
