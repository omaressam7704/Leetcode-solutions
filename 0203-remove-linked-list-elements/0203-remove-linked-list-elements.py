class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Handle the case where the head is None
        if head is None:
            return None
        
        # Skip any initial nodes with value equal to val
        while head is not None and head.val == val:
            head = head.next

        # Return None if all nodes have value equal to val
        if head is None:
            return None
        
        # Remove nodes with value equal to val
        curr = head
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
