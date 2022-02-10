class MinStack:

    def __init__(self):
        self.min=1000
        self.stack=[]
        self.prevMin={}


    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        if val < self.min:
            self.prevMin[val] = self.min
            self.min = val

    def pop(self) -> None:
        n=self.stack.pop(0)
        if n == self.min:
            self.min = self.prevMin[n]
            self.prevMin.pop(n)

        return n

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(1);
minStack.push(2);
minStack.push(4);
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
print(minStack.pop())
print(minStack.pop())
#print(minStack.top())
