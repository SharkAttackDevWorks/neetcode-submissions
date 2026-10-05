# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return []
        output = []
        alist = deque()
        alist.append(root)

        while alist:
            level = []
            for _ in range(len(alist)):
                root = alist.popleft()
                level.append(root.val)
                if root.left:
                    alist.append(root.left)
                if root.right:
                    alist.append(root.right)
            output.append(level)
            level=[]

        return output
            
