class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        # prev        curr
        #  ↓           ↓
        # None       [1] -> [2] -> [3] -> None

        while curr:
            temp = curr.next # Save temp

            # Reverse pointer
            # prev      curr
            #  ↓         ↓
            # None <--- [1]    [2] -> [3]
            curr.next = prev


            # Move both forward
            prev = curr
            curr = temp

            #      prev       curr
            #       ↓          ↓
            # None <-[1]      [2] -> [3]

        # prev
        #  ↓
        # [3] -> [2] -> [1] -> None

        return prev