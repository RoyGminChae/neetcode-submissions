class MinStack:

    def __init__(self):
        self.stack = []
        self.minValMap = {} # {index: minVal at that point}
        self.minVal = None

    def push(self, val: int) -> None:
        if self.minVal is None or val < self.minVal:
            self.minVal = val

        self.stack.append(val)
        self.minValMap[len(self.stack) - 1] = self.minVal
        


    def pop(self) -> None:
        self.minValMap.pop(len(self.stack) - 1)
        self.stack.pop()
        
        if self.stack:
            self.minVal = self.minValMap[len(self.stack) - 1]
        else:
            self.minVal = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
