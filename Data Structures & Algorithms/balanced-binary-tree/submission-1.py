# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def bfs(root):

            if root is None:
                return 0
            
            diff = 0

            L = root.left
            R = root.right

            if L is not None and R is not None:
                diff += max(bfs(R), bfs(L))
            elif L is not None:
                diff += 1 + bfs(L)
            elif R is not None:
                diff += 1 + bfs(R)
            else:
                diff +=0

            print(diff)

            return diff

        
        return bfs(root) <= 1