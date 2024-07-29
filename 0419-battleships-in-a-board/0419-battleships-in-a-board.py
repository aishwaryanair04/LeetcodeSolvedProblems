class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        res =[]
        count = 0
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    if (i > 0 and board[i-1][j]) == 'X':
                        continue
                    if (j > 0 and board[i][j-1]) == 'X':
                        continue
                    
                    res.append((i,j))
                    count+= 1
        
        print(res)
        return count
                    
                        
            
                        
                            
                    
                
        