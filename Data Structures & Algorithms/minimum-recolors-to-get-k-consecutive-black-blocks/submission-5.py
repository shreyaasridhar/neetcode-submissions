class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i ,j = 0, k # two pointer reference
        wCt = 0
        for x in range(i,j):
            if blocks[x] == 'W':
                wCt += 1
        minW = wCt
        while j < len(blocks):
            if blocks[i] == 'W':
                wCt -= 1
            i += 1
            if blocks[j] == 'W':
                wCt += 1
            minW = min(minW, wCt)
            j += 1
        return minW


        # minW updates when you find the least W
        # [WBBWWBB]WBW
        # w= 3
        # W[BBWWBBW]BW
        # w -1 + 1 = 3
        # WB[BWWBBWB]W
        # w - 0 + 0 = 3
        # WBB[WWBBWBW]
        # w - 0 + 1 = 4
        # leastW = 3
        # [WWWWWB]BWWWBWB