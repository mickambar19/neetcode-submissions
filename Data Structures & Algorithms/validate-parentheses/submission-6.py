class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        
        stack = []
        for bracket in s:
            if bracket not in pair:
                stack.append(bracket)
            elif stack and stack[-1] == pair[bracket]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
            