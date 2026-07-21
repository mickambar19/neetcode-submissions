class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights.append(0)
        for idx in range(len(heights)): 
            height = heights[idx]
            lastIdx = idx
            while stack and stack[-1][1] > height:
                prevIdx, prevHeight = stack.pop()
                maxArea = max(maxArea, prevHeight * (idx - prevIdx))    
                lastIdx = prevIdx    
            stack.append((lastIdx, height))
        return maxArea