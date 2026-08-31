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
        if zeroct == len(nums):
            return [0]*zeroct
        print(all_product)
        for i, num in enumerate(nums):
            if num == 0:
                if zeroct <= 1:
                    product.append(all_product)
                else:
                    product.append(0)
            if num != 0:
                if zeroct > 0:
                    product.append(0)
                else:
                    product.append(int(all_product/num))
        return product