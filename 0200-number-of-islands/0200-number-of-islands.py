class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(i, j):
            q = collections.deque()
            vis.add((i,j))
            q.append((i,j))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for r, c in directions:
                    if (row+r >=0 and col+c >= 0 and row+r < len(grid) and col+c < len(grid[0]) and
                        grid[row + r][col+c] == "1" and (row+r, col+c) not in vis):
                        q.append((row+r, col+c))
                        vis.add((row+r, col+c))
        
        rows, cols = len(grid), len(grid[0])
        vis = set()
        res = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in vis:
                    res += 1
                    bfs(i, j)
        return res
                        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         adjLs = [[] for _ in range(len(grid))]
        
#         for i in range(len(grid)):
#             for j in range(len(grid)):
#                 if grid[i][j] == 1 and i != j:
#                     adjLs[i].append(j)
#                     adjLs[j].append(i)
        
#         vis = [0]*len(grid)
#         res = 0
        
#         for i in range(len(grid)):
#             if not vis[i]:
#                 res += 1
#                 self.dfs(i, adjLs, vis)
        
#         return res
    
#     def dfs(self, node, adjLs, vis):
#         vis[node] = 1
        
#         for neightbor in adjLs[node]:
#             if not vis[neighbor]:
#                 self.dfs(neighbor, adj, vis)
        