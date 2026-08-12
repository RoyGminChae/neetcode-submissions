import heapq

# Interval Visualization
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = dict()

        minHeap = [] # (size, end of interval)
        i = 0 # intervals index
        for query in sorted(queries):
            # add all intervals to heap up to query
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(minHeap, (size, end))
                i += 1

            # remove all intervals from heap that doesn't overlap with query
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            # now minHeap[0][0] is the smallest interval compatiable with query
            res[query] = minHeap[0][0] if minHeap else -1

        return [res[query] for query in queries]

