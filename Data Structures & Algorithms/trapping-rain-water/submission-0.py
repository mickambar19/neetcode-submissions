class Solution:
    def trap(self, height: List[int]) -> int:
        left_bar = [0] * (len(height) + 1)
        right_bar = [0] * (len(height) + 1)
        for i in range(1, len(height)):
            if height[i-1] > left_bar[i-1]:
                left_bar[i] = height[i-1]
            else:
                left_bar[i] = left_bar[i-1]

        for i in range(len(height) - 2, -1, -1):
            if height[i+1] > right_bar[i+1]:
                right_bar[i] = height[i+1]
            else:
                right_bar[i] = right_bar[i+1]
        
        total = 0
        for i in range(len(height)):
            total += max(min(left_bar[i], right_bar[i]) - height[i], 0)
        return total

        

        
        
        