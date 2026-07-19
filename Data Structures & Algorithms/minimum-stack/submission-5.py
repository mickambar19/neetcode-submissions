class Node:
    def __init__(self, val=None, next_=None):
        self.val= val
        self.next_ = next_

class MinStack:

    def __init__(self):
        self.stack = None
        self.min_stack = None

    def push(self, val: int) -> None:
        if self.stack:
            self.stack = Node(val, self.stack)
        else:
            self.stack = Node(val)

        if self.min_stack:
            min_val = self.min_stack.val
            self.min_stack = Node(min(min_val, val), self.min_stack)
        else:
            self.min_stack = Node(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        element = self.stack 
        self.stack = self.stack.next_
        self.min_stack = self.min_stack.next_
        return element.val

    def top(self) -> int:
        return self.stack.val if self.stack else None
        

    def getMin(self) -> int:
        return self.min_stack.val if self.min_stack else None
        
