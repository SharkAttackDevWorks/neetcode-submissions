# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        start = root
        def inverter(root):
            if root is None:
                return

            L = root.left
            R = root.right

            root.left = inverter(R) if R is not None else None
            root.right = inverter(L) if L is not None else None

            return root

        inverter(root)

        return start