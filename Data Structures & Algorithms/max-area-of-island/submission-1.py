class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        visit = set()

        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visit.add((r, c))
            area = 1

            while q:
                
                row, col = q.popleft()

                for dr, dc in DIRS:
                    new_r, new_c = row + dr, col + dc

                    if (new_r in range(ROWS) and new_c in range(COLS)
                        and grid[new_r][new_c] == 1 and (new_r, new_c) not in visit):

                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))
                        area += 1
            
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
