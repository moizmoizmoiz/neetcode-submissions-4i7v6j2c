# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        original_head = head

        while head:
            nodes.append(head)
            head = head.next

        if len(nodes) == 1:
                return None        



        remove = len(nodes) - n
        nodes.pop(remove)

        if remove == 0:
            return original_head.next

        for i in range(len(nodes)):
            if i == len(nodes) - 1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
        
        return original_head





