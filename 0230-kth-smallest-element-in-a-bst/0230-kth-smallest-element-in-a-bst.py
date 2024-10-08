# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return None
        
        res = []
        curr = root
        stack = []
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res[k-1]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         stack = []
#         curr = root
        
#         while stack or curr:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             res.append(curr.val)
#             curr = curr.right
        
#         return res[k-1]
                    
                    
            
            
                
                
        