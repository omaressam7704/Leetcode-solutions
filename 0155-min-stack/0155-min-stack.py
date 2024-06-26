class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.top_=-1
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.top_+=1
        self.stack.append(val)
    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.top_-=1
    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.top_]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return min(self.stack)
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()