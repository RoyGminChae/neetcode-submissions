# think of kinda like dijkstra where I'm updating the neighbor nodes 
# if their jumps is already less than what is already set
# you move to the next index node instead of using minHeap like dijkstra

# bfs

class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps = [0] + [float('inf')] * (len(nums) - 1)
        for i, jump in enumerate(nums):
            for j in range(1, jump + 1):
                if i + j >= len(nums):
                    break
                
                minJumps[i + j] = min(minJumps[i + j], minJumps[i] + 1)
        
        return minJumps[-1]