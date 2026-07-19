class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        '{}'
        stack = []
        for bracket in s:
            if bracket in pair and len(stack):
                if stack[-1] == pair[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0
            