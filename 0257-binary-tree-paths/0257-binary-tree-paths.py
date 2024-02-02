# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        
        def dfs(node, path):
            if not node:
                return None
            
            if not node.left and not node.right:
                path.append(str(node.val))
                ans.append("->".join(str(s) for s in path))
                path.pop()
                return
            
            path.append(str(node.val))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        return ans
            
        
        
        