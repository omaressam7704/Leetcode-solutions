# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def count(self, head):
        trav = head
        cnt = 0
        while trav is not None:
            cnt+=1
            trav = trav.next
        return cnt
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cnt = self.count(head)
        if(cnt == 2):
            head.next = None
            return head
        elif(cnt == 1):
            head = None
            return head
        cnt = cnt // 2
        if cnt % 2 == 0:
            trav = head
            i = 0
            for i in range(cnt-1):
                trav = trav.next
            trav.next = trav.next.next
        else:
            trav = head
            i = 0
            for i in range(cnt-1):
                trav = trav.next
            trav.next = trav.next.next
        return head