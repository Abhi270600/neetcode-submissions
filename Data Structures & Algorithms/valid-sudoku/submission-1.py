class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        rowset = collections.defaultdict(set)
        colset = collections.defaultdict(set)
        boxset = collections.defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                
                val = board[r][c]
                
                if val == ".":
                    continue
                
                if val in rowset[r] or val in colset[c] or val in boxset[(r//3, c//3)]:
                    return False
                
                rowset[r].add(val)
                colset[c].add(val)
                boxset[(r//3, c//3)].add(val)
        
        return True
                    