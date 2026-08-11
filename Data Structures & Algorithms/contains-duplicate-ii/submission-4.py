class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = 0
        for i, val in enumerate(nums):
            if i - l > k:
                seen.remove(nums[l])
                l += 1
            if val in seen:
                return True
            seen.add(val)
        return False
