class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def check(r, c):
            nonlocal fresh
            if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))
                fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        

        time = 0
        while q and fresh > 0:
            n = len(q)
            for _ in range(n):
                row, col = q.popleft()

                check(row + 1, col)
                check(row - 1, col)
                check(row, col + 1)
                check(row, col - 1)
            
            time += 1
        
        return time if fresh == 0 else -1

