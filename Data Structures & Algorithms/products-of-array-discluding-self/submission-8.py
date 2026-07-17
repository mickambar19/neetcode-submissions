class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        results = [1] * length
        prefix = 1
        for i in range(1, length):
            results[i] = prefix * nums[i-1]
            prefix = prefix * nums[i-1]
        posfix = 1
        for i in range(length - 1, -1, -1):
            results[i] = results[i] * posfix
            posfix = posfix * nums[i]

        return results