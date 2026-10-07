class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        i = 1
        j = 0
        res.append(intervals[0])
        while i < len(intervals):
            f, s = res[j], intervals[i]
            if f[1] >= s[0]: # overlap
                res.pop()
                res.append([min(f[0], s[0]), max(f[1], s[1])])
            else:
                res.append(intervals[i])
                j += 1  
            i += 1
        return res