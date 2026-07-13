class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for n in nums:
            if n not in frequencies:
                frequencies[n] = 0
            frequencies[n] += 1
        
        freqTuple = [(freq, num) for num, freq in frequencies.items()] 
        
        elements = []
        idx = 0
        for _, num in sorted(freqTuple, reverse=True):
            elements.append(num)
            idx+=1
            if idx == k:
                return elements
        return elements 