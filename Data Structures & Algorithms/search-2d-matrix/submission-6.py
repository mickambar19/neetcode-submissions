class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1

        while lo <= hi:
            row = (lo + hi) // 2
            if target > matrix[row][-1]:
                lo = row + 1
            elif target < matrix[row][0]:
                hi = row - 1
            else:
                break

        if lo > hi:
            return False

        row = (lo + hi) // 2
        lo, hi = 0, len(matrix[0]) - 1
        while lo <= hi:
            col = (lo + hi)// 2
            if target > matrix[row][col]:
                lo = col + 1
            elif target < matrix[row][col]:
                hi = col - 1
            else:
                return True
                
        return False