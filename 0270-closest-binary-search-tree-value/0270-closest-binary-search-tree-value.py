# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        curr = root.val if root else None
        while root:
            if abs(root.val - target) < abs(curr - target):
                curr = root.val
            elif abs(root.val - target) == abs(curr - target):
                curr= min(root.val, curr)
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return curr
        
        