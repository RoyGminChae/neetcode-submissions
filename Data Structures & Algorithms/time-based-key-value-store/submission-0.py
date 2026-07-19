from collections import defaultdict

# upper bound search
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
    

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap[key]

        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if timestamp < arr[mid][1]:
                right = mid
            else:   
                left = mid + 1
        
        if left == 0:
            return ""
        else:
            return arr[left-1][0]
        