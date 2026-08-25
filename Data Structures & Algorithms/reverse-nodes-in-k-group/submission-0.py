# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        def reverser(oldhead, k):

            curr = oldhead
            prev = None
            while k > 0 and curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k-=1

            newhead = prev
            nextnode = curr

            return oldhead, newhead, nextnode

        def has_k(head, k):

            while head is not None and k >0:
                head = head.next
                k-=1
            
            if k > 0:
                return False
            return True



        prev_tail = ListNode()

        oldhead, newhead, nextnode = reverser(head, k)
        start = newhead
        head = nextnode
        prev_tail = oldhead
        
        while has_k(head, k):
            oldhead, newhead, nextnode = reverser(head, k)
            prev_tail.next = newhead
            oldhead.next = nextnode
            head = nextnode

        if head is not None:
            prev_tail.next = head

        return start





