# monotonic stack pattern
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)
        for i in range(len(temps)):
            temp = temps[i]
            while stack and temp > temps[stack[-1]]:
                warmerThanThisDay = stack.pop()
                res[warmerThanThisDay] = i - warmerThanThisDay
            stack.append(i)

        return res




# if not stack or temp <= stack[-1]:
#                 stack.append(i)
#             else: