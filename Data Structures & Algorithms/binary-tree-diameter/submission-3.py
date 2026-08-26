# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        best = [0]

        def height(node):
            if node is None:
                return 0

            L = height(node.left)
            R = height(node.right)

            best[0] = max(best[0], L+R)


            return 1 + max(L, R) 

        def diameter(root):

            if root is None:
                return
            
            L = height(root.left)
            R = height(root.right)

            best[0] = max(best[0], L+R)

            diameter(root.left)
            diameter(root.right)


        # diameter(root)
        height(root)

        return best[0]
