class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self.head.next
        cnt = 0
        while cur and cnt < index:
            cur = cur.next
            cnt += 1
        if cnt == index and cur:
            return cur.val
        else:
            return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        if self.tail == self.head:
            self.tail = new

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new = ListNode(val)
        self.tail.next = new
        self.tail = new
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= 0:
            self.addAtHead(val)
        elif index == self.count():
            self.addAtTail(val)
        elif index > self.count():
            return
        else:
            new = ListNode(val)
            cnt = 0
            trav = self.head
            while cnt < index:
                trav = trav.next
                cnt += 1
            new.next = trav.next
            trav.next = new

    def count(self):
        cnt = 0
        trav = self.head.next
        while trav is not None:
            trav = trav.next
            cnt += 1
        return cnt

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.count():
            return
        elif index == 0:
            self.head.next = self.head.next.next
            if not self.head.next:
                self.tail = self.head
        else:
            cnt = 0
            trav = self.head
            while cnt < index:
                trav = trav.next
                cnt += 1
            trav.next = trav.next.next
            if not trav.next:
                self.tail = trav

