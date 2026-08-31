class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        product = []
        zeroct = 0
        for num in nums:
            if num != 0:
                all_product *= num
            else:
                zeroct += 1
        if zeroct > 1:
            return [0]*len(nums)
        for i, num in enumerate(nums):
            if zeroct:
                if num == 0:
                    product.append(all_product)
                else:
                    product.append(0)
            else:
                product.append(all_product//num)
        return product