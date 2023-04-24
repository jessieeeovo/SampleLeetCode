import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x <= y:
                heapq.heappush(stones, x - y)
        return -stones[0]