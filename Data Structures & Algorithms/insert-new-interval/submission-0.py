class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []
        while i < n and intervals[i][0] <= newInterval[0]:
            res.append(intervals[i])
            i += 1
        j = i 
        # print(i,j,res)
        if j == 0:
            res.append(newInterval)
            j+=1
        f, s = res[j-1], newInterval
        if f[1] >= s[0]:
            res.pop()
            res.append([min(f[0], s[0]), max(f[1],s[1])])
        else:
            res.append(newInterval)
            j+=1
        while i < n:
            f, s = res[j - 1], intervals[i]
            if f[1] >= s[0]:
                res.pop()
                res.append([min(f[0], s[0]), max(f[1],s[1])])
            else:
                res.append(intervals[i])
                j += 1
            i += 1

        return res