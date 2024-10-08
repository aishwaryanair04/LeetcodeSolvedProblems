# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif not root.left and root.right:
                return root.right
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left
                
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        
        return root
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return
        
#         if key < root.val:
#             root.left = self.deleteNode(root.left, key)
#         elif key > root.val:
#             root.right = self.deleteNode(root.right, key)
#         else:
#             if not root.left and not root.right:
#                 return None
#             elif root.left and not root.right:
#                 return root.left
#             elif not root.left and root.right:
#                 return root.right
#             elif root.left and root.right:
#                 temp = root.right
#                 while temp.left:
#                     temp = temp.left
#                 root.val = temp.val
#                 root.right = self.deleteNode(root.right, temp.val)
        
#         return root
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return None
        
#         if key > root.val:
#             root.right = self.deleteNode(root.right, key)
#         elif key < root.val:
#             root.left = self.deleteNode(root.left, key)
#         else:
#             if not root.left and not root.right:
#                 return None
#             elif not root.left and root.right:
#                 return root.right
#             elif root.left and not root.right:
#                 return root.left
#             else:
#                 pnt = root.right
#                 while pnt.left:
#                     pnt = pnt.left
#                 root.val = pnt.val
#                 root.right = self.deleteNode(root.right, pnt.val)
            
#         return root
                
                