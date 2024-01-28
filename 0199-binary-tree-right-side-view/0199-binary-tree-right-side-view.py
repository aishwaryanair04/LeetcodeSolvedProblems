# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = collections.deque()
        res = []
        if root:
            queue.append(root)
        
        
        while queue:
            val = []
            for i in range(len(queue)):
                node = queue.popleft()
                print(node.val)
                val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(val)
        
        
        values = []
        for val in res:
            values.append(val[-1])
        
        return values
            
        