# this is a monotonic stack problem
# or can be solved by iteration (more direct)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        for pos, speed in pairs:
            time = (target - pos) / speed
            
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)