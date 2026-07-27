class Solution:
    # problem states: at most 1 solution
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # guarantees that 1 solution exist
        tank = 0
        station = 0
        for i in range(len(gas)): # watch the video of why I don't need to loop
            tank += gas[i] - cost[i]
            
            if tank < 0:
                tank = 0
                station = i + 1

        return station
