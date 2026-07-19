class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sequences = {}
        for num in nums:
            if num-1 in nums_set or num in sequences:
                continue
            sequences[num] = set([num])
            next_ = num+1
            while next_ in nums_set:
                sequences[num].add(next_)
                next_+=1
        longest = 0
        
        for key, value in sequences.items():
            if len(value)>longest:
                longest = len(value)
        return longest

            
            