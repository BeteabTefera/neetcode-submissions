class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.val = val
        self.stack.append(val)


    def pop(self) -> None:
        if len(self.stack) <= 0:
            return 'Cannot POP from an empty list'
        else:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
