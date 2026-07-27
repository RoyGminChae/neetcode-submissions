import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        counter = Counter(hand)
        for num in hand:
            if not counter[num]:
                continue
            
            for i in range(num, num + groupSize):
                if not counter[i]:
                    return False
                counter[i] -= 1
            
        return True



        
    
    # [1, 2, 2, 3, 3, 4, 4, 5]

    # [1, 2, 3, 3, 4, 5, 6, 7]