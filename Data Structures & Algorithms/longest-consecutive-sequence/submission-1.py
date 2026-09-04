class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sNums = sorted(nums)
        lSeq = ct = 1
        for i,s in enumerate(sNums):
            if i-1 >= 0 and (s - sNums[i-1] == 1):
                ct += 1
                lSeq = max(ct,lSeq)
            if i-1 > 0 and s - sNums[i-1] > 1:
                ct = 1
            # print(i,s,ct,lSeq)
        return lSeq