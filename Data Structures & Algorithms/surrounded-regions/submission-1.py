class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def bfs(r, c):
            
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                board[row][col] = 'T'

                for dr, dc in DIRS:
                    new_r, new_c = row + dr, col + dc

                    if (new_r in range(ROWS) and new_c in range(COLS) 
                        and board[new_r][new_c] == 'O'):
                        q.append((new_r, new_c))

        for r in range(ROWS):
            if board[r][0] == 'O':
                bfs(r, 0)
            
            if board[r][COLS - 1] == 'O':
                bfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == 'O':
                bfs(0, c)
            
            if board[ROWS - 1][c] == 'O':
                bfs(ROWS - 1, c)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                
                if board[r][c] == 'T':
                    board[r][c] = 'O'

