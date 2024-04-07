class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        trav = head
        if trav is None or trav.next is None:
            return head
        
        curr = trav
        trav = trav.next
        while trav is not None:
            if curr.val == trav.val:
                curr.next = trav.next
            else:
                curr = trav
            trav = trav.next
        return head
