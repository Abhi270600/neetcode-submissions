class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        res = []

        def dfs(r, c, ocean, prev_height):
            if (r < 0 or r == ROWS or c < 0 or c == COLS 
                or (r, c) in ocean or heights[r][c] < prev_height):
                return
            
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)
        
        for c in range(COLS):
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)
        
        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])
        
        return res
        