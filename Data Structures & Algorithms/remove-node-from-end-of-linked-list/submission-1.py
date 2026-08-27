# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # SLOW AND FAST POINTER METHOD
        # time - o(n) space - o(1)


        # Edge case: one 1 element in list
        # if head.next == None: return None 


        # original_head, slow, fast = head, head, head

        # j = n
        # while j > 0:
        #     fast = fast.next
        #     j -= 1

        
        # while fast and fast.next: # Edge case for when fast ends up being the last element or (None)
        #     slow = slow.next
        #     fast = fast.next

        # if n == 1: # Edge case for when last element is to be popped
        #     slow.next = None
        #     return original_head
        # elif slow == original_head: # Edge case for when first element is to be popped
        #     return original_head.next
        # else:
        #     slow.next = slow.next.next
        #     return original_head
        
        dummy = ListNode(0, head) # Initialise a dummy node 

        slow = fast = dummy 

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next