class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visit = set()

        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visit.add((r, c))

            while q:

                row, col = q.popleft()

                for dr, dc in DIRS:
                    new_r, new_c = row + dr, col + dc

                    if (new_r in range(ROWS) and new_c in range(COLS) and
                        grid[new_r][new_c] == "1" and (new_r, new_c) not in visit):

                        visit.add((new_r, new_c))
                        q.append((new_r, new_c))

        
        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands
