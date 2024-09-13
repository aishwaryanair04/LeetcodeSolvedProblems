class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        adjLs = [[] for _ in range(len(isConnected))]
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i!= j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
        print(adjLs)
        
        vis = [0]*len(isConnected)
        res = 0
        
        for i in range(len(isConnected)):
            if not vis[i]:
                res += 1
                self.dfs(i, adjLs, vis)
        return res
        
        
        
    def dfs(self, node, adjLs, vis):
        vis[node] = 1
        
        for neighbor in adjLs[node]:
            if not vis[neighbor]:
                self.dfs(neighbor, adjLs, vis)
            
                 
        