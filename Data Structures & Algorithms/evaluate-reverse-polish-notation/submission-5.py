class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: x+y, 
            '-': lambda x, y: x-y, 
            '*': lambda x, y: x*y, 
            '/': lambda x, y: int( x/y) if y != 0 else 0
        }
        stack = []

        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                stack.append(operators[token](x, y))
            else: 
                stack.append(int(token))
        return stack.pop()