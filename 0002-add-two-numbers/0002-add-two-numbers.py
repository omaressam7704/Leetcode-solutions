# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        temp1 = l1
        temp2 = l2
        head = ListNode()
        temp = head
        x1 = []
        x2 = []
        while temp1.next is not None:
            x1.append(temp1.val)
            temp1 = temp1.next
        x1.append(temp1.val)
        while temp2.next is not None:
            x2.append(temp2.val)
            temp2 = temp2.next
        x2.append(temp2.val)
        x1.reverse()
        x2.reverse()
        num1 = int(''.join(map(str, x1)))
        num2 = int(''.join(map(str, x2)))
        total_sum = num1 + num2
        sum_str = str(total_sum)
        for digit in sum_str[::-1]:
            temp.next = ListNode(int(digit))
            temp = temp.next
            
        return head.next
