class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        n = len(self.stack)
        m = len(self.minStack)
        if m > 0 and n > 0 and self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minStack) > 0:
            return self.minStack[-1]