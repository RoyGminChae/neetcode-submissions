"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)
        rooms = [0]  # (earliest end time)
        for interval in intervals:
            if rooms[0] <= interval.start:
                heapq.heapreplace(rooms, interval.end)
            else:
                heapq.heappush(rooms, interval.end)
        
        return len(rooms)
                
            


