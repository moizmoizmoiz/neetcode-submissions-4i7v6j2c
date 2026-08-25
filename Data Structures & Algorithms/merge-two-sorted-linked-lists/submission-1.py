# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode() #dummy is anchor to return the answer and node is just what we traverse here

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next # move list1 to next
            else:
                node.next = list2 # since we are not building in place we can just check if 
                                  # val < val2 . dont have to check for value ahead.
                list2 = list2.next
            node = node.next # moving ahead

        node.next = list1 or list2 # whichever non empty

        return dummy.next # return the anchor