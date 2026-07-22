import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = stones[:]
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush_max(stones, y)
            else:
                x = x - y
                heapq.heappush_max(stones, x)

        return stones[0] if stones else 0



