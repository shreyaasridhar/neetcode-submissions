class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def noHours(speed, piles):
            hours = 0
            for banana in piles:
                hours += math.ceil(banana / speed)
            return hours
        l , r = 1, max(piles)
        res = r
        while l < r:
            mid = (l+r) // 2
            if noHours(mid, piles) <= h:
                res = mid
                r = mid
            else:
                l = mid + 1
        return res
