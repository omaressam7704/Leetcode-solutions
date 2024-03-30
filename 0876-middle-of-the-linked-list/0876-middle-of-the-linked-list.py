# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def count(self,head):
        cnt = 0
        trav = head
        while trav is not None:
            trav = trav.next
            cnt+=1
        return cnt
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        trav = head
        prev = trav
        cnt = self.count(head) //2
        for i in range(cnt):
            prev = trav
            trav = trav.next
        prev.next = None
        return trav