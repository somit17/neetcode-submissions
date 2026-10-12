class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # First, create a copy of the original head to preserve the original list
        original = head
        
        # Reverse the linked list
        reversed_head = self.reverseLinkedList(self.copyList(head))
        
        # Compare the original and reversed lists
        while original and reversed_head:
            if original.val != reversed_head.val:
                return False
            original = original.next
            reversed_head = reversed_head.next
        
        return True
    
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseLinkedList(head.next)
        
        # Reverse the connection
        head.next.next = head
        head.next = None
        
        return new_head
    
    def copyList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a deep copy of the linked list
        if not head:
            return None
        
        new_head = ListNode(head.val)
        new_head.next = self.copyList(head.next)
        
        return new_head
