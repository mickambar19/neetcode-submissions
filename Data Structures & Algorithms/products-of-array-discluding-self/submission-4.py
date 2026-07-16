class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        posfix = []
        i = 0
        length = len(nums)
        while i < length:
            prev = prefix[i-1] if i != 0 else 1
            prevPosfix = posfix[i-1] if i != 0 else 1

            prefix.append(prev * nums[i])
            posfix.append(prevPosfix * nums[length - i - 1])
            i+=1
        print(prefix, posfix)
        i = 0
        result = []
        posfix = posfix[::-1]
        while i < length:
            prefixValue = prefix[i-1] if i != 0 else 1
            posfixValue = posfix[i+1] if i != length -1 else 1
            result.append(prefixValue * posfixValue)
            i+=1
        return result
