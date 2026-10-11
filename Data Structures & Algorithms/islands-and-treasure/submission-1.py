class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def check(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS 
                or grid[r][c] != 2147483647 or (r, c) in visit):
                return

            q.append((r, c))
            visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 0
        while q:
            n = len(q)
            for _ in range(n):
                row, col = q.popleft()
                grid[row][col] = dist

                check(row + 1, col)
                check(row - 1, col)
                check(row, col + 1)
                check(row, col - 1)
            
            dist += 1

