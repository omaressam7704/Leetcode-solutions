class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        odd_head, even_head = head, head.next
        odd_ptr, even_ptr = odd_head, even_head
        
        while even_ptr and even_ptr.next:
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next

        odd_ptr.next = even_head

        return odd_head
