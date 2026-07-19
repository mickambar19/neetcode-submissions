class Node:
    def __init__(self, val=None, next_=None):
        self.val= val
        self.next_ = next_

class MinStack:

    def __init__(self):
        self.stack = Node()
        self.min_stack = Node()

    def push(self, val: int) -> None:
        node = Node(val, self.stack.next_)
        self.stack.next_ = node
        if self.min_stack.next_:
            min_val = self.min_stack.next_.val
            self.min_stack.next_ = Node(min(min_val, val), self.min_stack.next_)
        else:
            self.min_stack.next_ = node

    def pop(self) -> None:
        if not self.stack.next_:
            return None
        old = self.min_stack.next_
        self.min_stack.next_ = old.next_
        old = None
        element = self.stack.next_
        self.stack.next_ = element.next_
        val = element.val
        element = None
        return val

    def top(self) -> int:
        return self.stack.next_.val
        

    def getMin(self) -> int:
        return self.min_stack.next_.val
        
