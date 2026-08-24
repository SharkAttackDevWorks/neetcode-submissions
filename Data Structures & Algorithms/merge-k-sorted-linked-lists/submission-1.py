# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # lists = [x for x in lists if len(x) > 0]

        # if len(lists) < 1:
        #     return []

        
        heap = []
        
        count = 0
        for x in lists:
            if x is not None:
                heapq.heappush(heap,[x.val, count, x])
                count+=1

        dummy = ListNode()
        head = dummy



        while len(heap) > 0:
            
            top = heapq.heappop(heap)

            node = top[2]

            dummy.next = node
            dummy = dummy.next


            if node.next is not None:
                top[2] = node.next
                top[0] = top[2].val

                # print(top)
                heapq.heappush(heap, top)



            
        
        return head.next



