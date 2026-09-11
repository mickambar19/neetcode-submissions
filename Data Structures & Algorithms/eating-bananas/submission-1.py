class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1
        candidate = hi

        while lo <= hi:
            mid = (hi + lo) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h and mid < candidate:
                candidate = mid 
            if hours > h:
                lo = mid + 1
            else: 
                hi = mid - 1
        return candidate

        