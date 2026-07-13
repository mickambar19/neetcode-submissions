class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        min_heap = []
        for n, frequency in freq.items():
            heapq.heappush(min_heap, (frequency, n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [n for _, n in min_heap]
        