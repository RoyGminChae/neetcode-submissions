import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = list(counter.values())
        heapq.heapify_max(maxHeap)
        queue = deque() # (count, idleTime)

        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap: 
                count = heapq.heappop_max(maxHeap) - 1
                if count > 0:
                    queue.append((count, time + n))
                
            if queue:
                count, idleTime = queue[0]
                if time == idleTime:
                    queue.popleft()
                    heapq.heappush_max(maxHeap, count)
        
        return time

        
        
