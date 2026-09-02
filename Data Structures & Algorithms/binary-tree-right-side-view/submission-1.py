# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        
        q = deque()
        q.append(root)

        if not root: return []

        while q:
            level = []
            for _ in range(len(q)):
                # print(q)
                node = q.popleft()
                level.append(node)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            output.append([x.val for x in level])

        result = []
        for x in output:
            result.append(x[-1])

        return result