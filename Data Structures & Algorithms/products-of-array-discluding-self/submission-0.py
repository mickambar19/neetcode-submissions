class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        while i < len(nums):
            j = 0
            total = 1
            while j < len(nums):
                if i != j:
                    total *= nums[j]
                j+=1
            result.append(total)
            i+=1
        return result
        
        