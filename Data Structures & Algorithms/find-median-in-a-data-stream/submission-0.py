import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] # max Heap
        self.right = [] # min Heap

    def addNum(self, num: int) -> None:
        # equal length
        # something must be added to left
        if len(self.left) <= len(self.right): 
            if self.right and num <= self.right[0]: # num belongs in left
                heapq.heappush_max(self.left, num)
            else: # num belongs in right
                heapq.heappush(self.right, num)       
                heapq.heappush_max(self.left, heapq.heappop(self.right))
        
        # left > right
        # something must be added to right
        else: 
            if num >= self.left[0]: # num belongs on right
                heapq.heappush(self.right, num)
            else: # num belongs on left
                heapq.heappush_max(self.left, num)
                heapq.heappush(self.right, heapq.heappop_max(self.left))


    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (self.left[0] + self.right[0]) / 2
        else:
            return self.left[0]

