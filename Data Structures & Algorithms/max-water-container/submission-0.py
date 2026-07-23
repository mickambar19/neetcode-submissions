class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAreaResult = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                maxAreaResult = max(area, maxAreaResult)
        return maxAreaResult