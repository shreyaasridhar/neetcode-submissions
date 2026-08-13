class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x
        mid = l+(r-l) // 2
        
        while l <= r:
            # print(l,r,mid)
            sqMid = mid * mid
            if sqMid == x:
                return mid
            elif sqMid < x:
                l = mid+1
            else:
                r = mid-1
            mid = l+(r-l) // 2
        return l - 1

        # def binarySearch(l, r):
        #     mid = l+(r-l) // 2
        #     sqMid = mid * mid
        #     if sqMid == x:
        #         return mid
        #     elif sqMid < x:
        #         return binarySearch(l+1, r)
        #     else:
        #         return binarySearch(l, r-1)
        #     return l
        # return binarySearch(1,x)