class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        orderedStack = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while orderedStack and orderedStack[-1][0] < temperatures[i]:
                _, idx = orderedStack.pop()
                results[idx] = i - idx
            orderedStack.append((temperatures[i], i))
        return results