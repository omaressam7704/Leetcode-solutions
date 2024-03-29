class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        trav1,trav2 = list1,list2
        head = ListNode()
        new = head
        while trav1 and trav2 is not None:
            if trav1.val < trav2.val:
                new.next = trav1
                new = trav1
                trav1 = trav1.next
            else:
                new.next = trav2
                new = trav2
                trav2 = trav2.next 
        new.next = trav1 or trav2
        head = head.next
        return head