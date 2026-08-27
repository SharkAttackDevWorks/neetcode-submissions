# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def same(tree, sub):

            if tree is None and sub is None:
                return True


            if tree is None:
                return False
            
            elif sub is None:
                return False

            if tree.val != sub.val:
                return False

            L = same(tree.left, sub.left)
            R = same(tree.right, sub.right)

            return L and R

        return same(root.left, subRoot) or same(root.right, subRoot)