class NestedIterator:

    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        self.hasNext()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            x = self.stack.pop()
            self.stack.extend(x.getList()[::-1])

        return len(self.stack) > 0