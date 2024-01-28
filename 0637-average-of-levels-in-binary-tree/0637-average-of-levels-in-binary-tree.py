# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = collections.deque()
        res = []
        
        if root:
            q.append(root)
            
        while q:
            val = []
            
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    val.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            add = 0
            if val:
                for num in val:
                    add += num
            
                avg = add/len(val)
                res.append(avg)
        
        return res
                
            
            
            
            
            
        
        
        