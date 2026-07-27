class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        ma, mb, mc = 0, 0, 0 
        for a, b, c in triplets:
            if a > ta or b > tb or c > tc:
                continue
            
            ma, mb, mc = max(ma, a), max(mb, b), max(mc, c)

        return [ma, mb, mc] == target
