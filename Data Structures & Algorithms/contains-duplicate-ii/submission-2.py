class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        L = 0
        for i, num in enumerate(nums):
            if i-L > k:
                seen.remove(nums[L])
                L += 1
            if num in seen and i-L <= k:
                return True
            seen.add(num)
        return False