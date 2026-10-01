class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            l1 = heapq.heappop(stones)
            l2 = heapq.heappop(stones)
            if l1 != l2:
                heapq.heappush(stones, l1 - l2)
        if not stones:
            return 0
        return -stones[0]