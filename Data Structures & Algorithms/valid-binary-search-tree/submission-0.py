# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node:
                val = node.val
                L = float('-inf')
                R = float('inf')

                if node.left: L = node.left.val
                if node.right: R = node.right.val

                if L > val or R < val:
                    return False

                return dfs(node.left) and dfs(node.right)

            return True

        return dfs(root)