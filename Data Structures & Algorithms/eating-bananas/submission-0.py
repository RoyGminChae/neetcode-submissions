import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        
        left = 1
        right = res
        while left <= right:
            k = (left + right) // 2

            time = 0 # times it takes to eat all the bananas
            for num in piles:
                time += math.ceil(num / k)

            if time <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res
        
        