class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            l1 = heapq.heappop_max(stones)
            l2 = heapq.heappop_max(stones)
            heapq.heappush_max(stones, abs(l1 - l2))
        return heapq.heappop_max(stones)