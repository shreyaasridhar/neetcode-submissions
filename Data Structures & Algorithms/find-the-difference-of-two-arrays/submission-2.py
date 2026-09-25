class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set, nums2Set = set(nums1), set(nums2)
        ans = [[],[]]
        for i in nums1Set:
            if i not in nums2Set:
                ans[0].append(i)
        
        for i in nums2Set:
            if i not in nums1Set:
                ans[1].append(i)
        return ans