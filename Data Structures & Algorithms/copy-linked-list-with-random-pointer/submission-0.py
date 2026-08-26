"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        start = head
        output = newnode = Node(head.val, head.next, head.random)
        clones = {head : newnode}
        head = head.next

        while head is not None:
            newnode = Node(head.val, head.next, head.random)
            clones[head] = newnode
            head = head.next
        


        for oldnode in clones:
            newnode = clones[oldnode] 
            newnode.next = clones[oldnode.next]if oldnode.next is not None else None
            newnode.random = clones[oldnode.random] if oldnode.random is not None else None

        return output

        