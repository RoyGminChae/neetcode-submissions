import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        inverse_count_map = defaultdict(list)
        for num in count_map:
            inverse_count_map[count_map[num]].append(num)

        iterable = sorted(list(inverse_count_map.items()), reverse=True)
        topK = 0
        output = []
        for count, nums in iterable:
            if topK >= k:
                break
            output.extend(nums) # can extend the whole list bc solution is unique
            topK += len(nums)

        return output
            

