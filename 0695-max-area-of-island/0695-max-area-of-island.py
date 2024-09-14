class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0
        
        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            area = 0
            
            while q:
                area += 1
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [ 0,1], [0,-1]]
                for dr, dc in directions:
                    if (0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and
                        grid[r+dr][c+dc] == 1 and (r+dr, c+dc) not in visit):
                        q.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
            return area
                        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    res = max(res, bfs(i,j))

        return res
        