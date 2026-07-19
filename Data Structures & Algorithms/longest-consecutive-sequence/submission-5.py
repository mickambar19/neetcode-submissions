class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = sorted(set(nums))
        longest = curr = 1
        for i in range(1, len(nums_set)):
            if nums_set[i] == nums_set[i-1] + 1:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1
        return longest