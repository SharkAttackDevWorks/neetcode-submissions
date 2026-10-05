# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        step = 0
        queue = deque()
        queue.append(root)

        if root is None: return 0


        while len(queue)>0:
            aset = set(queue)
            step+=1
            
            for _ in range(len(queue)):
                root = queue.popleft()
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)

            
        return step