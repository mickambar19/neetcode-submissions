class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            results[i] = prefix
            prefix *= nums[i]

        posfix = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= posfix
            posfix *= nums[i]
        return results