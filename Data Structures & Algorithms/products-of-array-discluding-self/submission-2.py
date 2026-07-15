class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        i = 0
        while i < len(nums):
            prev = prefix[i-1] if i != 0 else 1
            prefix.append(nums[i] * prev)
            i+=1

        postfix = [1] * len(nums)
        i = len(nums) - 1
        while i >= 0:
            _next = postfix[i+1] if i != len(nums) - 1 else 1
            postfix[i] = nums[i] * _next
            i-=1

        result = []
        i = 0
        while i < len(nums):
            prefixValue = prefix[i - 1] if i != 0 else 1
            postfixValue = postfix[i + 1] if i != len(nums) - 1 else 1
            result.append(prefixValue * postfixValue)
            i+=1
        return result
            
