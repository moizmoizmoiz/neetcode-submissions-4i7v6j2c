# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next: # this is only so we can get to the midpoint
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        slow.next = None # End of the list -> Null



        # classic reversal algo

        prev = None
        while second:
            temp = second.next 
            second.next = prev
            prev = second
            second = temp


        second = prev


        # merging the 2 bointers
        first = head # starting point

        # going back and forth bing bang bing bang bing bang
        while second:
            temp1 = first.next 
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
