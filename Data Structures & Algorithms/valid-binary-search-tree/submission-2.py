# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, amax, amin):
            if node:
                val = node.val

                if not (amax > val > amin):
                    return False

                return dfs(node.left, val, amin) and dfs(node.right, amax, val)

            return True

        return dfs(root, float('inf'), float('-inf'))