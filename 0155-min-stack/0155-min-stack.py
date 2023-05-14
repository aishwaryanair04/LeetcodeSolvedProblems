class MinStack(object):

    def __init__(self):
        self.s=[]
        self.minstack=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.minstack==[]:
            self.minstack.append(val)
        else:
            if val <= self.minstack[-1]:
                self.minstack.append(val)
        self.s.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.s[-1] == self.minstack[-1]:
            del self.minstack[-1]
        
        del self.s[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()