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
        intervals.sort(key=lambda x: x.start)
        rooms = []  # (earliest end time)
        for interval in intervals:
            if rooms and rooms[0] <= interval.start:
                heapq.heapreplace(rooms, interval.end)
            else:
                heapq.heappush(rooms, interval.end)
        
        return len(rooms)
                
            


