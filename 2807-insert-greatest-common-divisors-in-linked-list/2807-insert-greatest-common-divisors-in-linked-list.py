class Solution(object):
    def gcd(self, a, b):
        g = 0
        k = 1
        while k <= min(a, b):
            if a % k == 0 and b % k == 0:
                g = k  
            k += 1
        return g  

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        trav = head
        if trav is None or trav.next is None:
            return head
        
        curr = trav
        trav = trav.next
        while trav is not None:
            x = self.gcd(curr.val, trav.val)
            new = ListNode(x, None)
            curr.next = new
            curr = curr.next  
            new.next = trav
            curr, trav = trav, trav.next
        return head
