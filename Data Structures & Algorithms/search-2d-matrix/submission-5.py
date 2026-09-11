class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, (m * n)
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            column = mid % n
            row = mid // n
            if matrix[row][column] == target:
                return True
            if matrix[row][column] > target: 
                hi = mid
            else:
                lo = mid + 1
        return False

