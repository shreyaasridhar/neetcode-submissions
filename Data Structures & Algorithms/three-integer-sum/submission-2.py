class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for ind,i in enumerate(nums):
            j,k = ind + 1, len(nums) - 1
            if ind > 1 and i == nums[ind-1]:
                continue
            diff = 0 - i
            while j < k:
                if nums[j] + nums[k] == diff:
                    if [i,nums[j], nums[k]] not in res:
                        res.append([i,nums[j], nums[k]])
                    k -= 1
                    j += 1
                elif nums[j] + nums[k] > diff:
                    k -= 1
                else:
                    j+=1
        return res

