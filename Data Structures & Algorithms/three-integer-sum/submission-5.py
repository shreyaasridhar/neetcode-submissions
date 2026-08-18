class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for ind,i in enumerate(nums):
            if i>0:
                break
            j,k = ind + 1, len(nums) - 1
            if ind > 0 and i == nums[ind-1]:
                continue
            diff = 0 - i
            while j < k:
                if nums[j] + nums[k] == diff:
                    res.append([i,nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: 
                        j += 1
                    while j < k and nums[k] == nums[k-1]: 
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > diff:
                    k -= 1
                else:
                    j+=1
        return res
