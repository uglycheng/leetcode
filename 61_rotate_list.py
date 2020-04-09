# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        count = 0
        pointer = head
        while pointer.next and k-count:
            pointer = pointer.next
            count += 1
        if not pointer.next:
            k = k%(count+1)
            pointer = head
            for count in range(k):
                pointer = pointer.next
        count = head  #still use count to save space, actually count has  diferent funciton, it serves as the slower pointer
        while pointer.next:
            pointer = pointer.next
            count = count.next
        pointer.next = head
        head = count.next
        count.next = None
        return head
        

        