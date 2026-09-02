# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = {}

        def dfs(node, level):
            if node:
                # print(node.val)
                if level in output:
                    output[level].append(node.val)
                else:
                    output[level] = [node.val]
                dfs(node.left, level+1)
                dfs(node.right, level+1)


        dfs(root, 0)

        result = [output[k] for k in sorted(output)]

        return result