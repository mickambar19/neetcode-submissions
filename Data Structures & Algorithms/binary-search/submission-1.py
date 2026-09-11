class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.r_search(nums, target, 0, len(nums) - 1)

    def r_search(self, nums: List[int], target: int, start: int, end: int)-> int:
        if start > end or end < start:
            return -1
        mid = start + ((end - start + 1) // 2)
        print(mid)
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            return self.r_search(nums, target, start, mid - 1)
        else: 
            return self.r_search(nums, target, mid + 1, end)
        return -1

# nums=[-1]
# target=2