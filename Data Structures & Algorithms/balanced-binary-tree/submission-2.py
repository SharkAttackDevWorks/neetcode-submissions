# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):

            if node is None:
                return [True, 0]
            L = dfs(node.left)
            R = dfs(node.right)

            bal = False
            if L[0] and R[0] and abs(L[1] - R[1]) <=1:
                bal = True

            return [bal, 1+max(L[1], R[1])]

        
        return dfs(root)[0]