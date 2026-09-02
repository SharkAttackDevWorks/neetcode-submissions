# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = 0
        amax = float('-inf')

        def dfs(node, amax):
            nonlocal good
            if node:
                if node.val >= amax:
                    print(node.val)
                    good+=1
                    amax = max(node.val, amax)
                dfs(node.left, amax)
                dfs(node.right, amax)
        

        dfs(root, amax)


        return good