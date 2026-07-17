class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        results = [1] * length
        # 2, 3, 4, 5 
        # 1, 2, 6, 24
        for i in range(1, length):
            results[i] = results[i - 1] * nums[i-1]
        # 2, 3, 4, 5 
        # 1, 2, 6, 24
        posfix = 1
        for i in range(length - 1, -1, -1):
            results[i] = results[i] * posfix
            posfix = posfix * nums[i]

        return results