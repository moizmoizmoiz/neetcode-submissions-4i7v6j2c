# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        values = set()

        # n = 0
        # while n <= 10:
        #     if head:
        #         print(head.val)
        #         head = head.next
        #         n += 1
        #     else:
        #         break
        
        while head: 
            if head not in values:
                values.add(head)
                head = head.next
            else:
                return True

        return False





