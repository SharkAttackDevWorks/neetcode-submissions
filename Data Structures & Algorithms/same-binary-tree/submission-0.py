# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def same(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            isTrue = True

            if p.val != q.val:
                isTrue = False
                print(p.val, q.val, False)

            L = same(p.left, q.left)
            R = same(p.right, q.right)

            return isTrue and L and R
        

        return same(p, q)