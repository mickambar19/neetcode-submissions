
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [value for value, _ in sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True)[0:k]]
        