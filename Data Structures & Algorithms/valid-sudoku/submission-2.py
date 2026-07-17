class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        group_cache = {} # (0,0): []
        row_cache = {} # 1: []
        column_cache = {}
        for row in range(len(board)):
            if row not in row_cache:
                row_cache[row] = []
            for col in range(len(board[0])):
                if board[row][col] == '.': 
                    continue
                    
                if col not in column_cache:
                    column_cache[col] = []

                group = (row//3, col//3)
                val = board[row][col]

                if group not in group_cache:
                    group_cache[group] = []

                
                if val in row_cache[row] or val in column_cache[col] or val in group_cache[group]:
                    return False
                row_cache[row].append(val)
                column_cache[col].append(val)
                group_cache[group].append(val)
                
        return True