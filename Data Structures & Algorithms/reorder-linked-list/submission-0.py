# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse_linkedlist(head):
            current = head
            prev = None 
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next

            return prev

        second = slow.next
        slow.next = None
        second = reverse_linkedlist(second)
        first, second_half = head, second
        while second_half:      #
            # Save next pointers
            tmp1, tmp2 = first.next, second_half.next
            
            # Reorder: first → second_half → rest of first
            first.next = second_half
            second_half.next = tmp1
            
            # Move pointers forward
            first, second_half = tmp1, tmp2

        