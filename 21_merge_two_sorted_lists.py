# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        result = l
        while l1 and l2:
            if l1.val > l2.val:
                l.next = l2
                l2 = l2.next
            else:
                l.next = l1
                l1 = l1.next
            l = l.next
        if l1:
            l.next = l1
        else:
            l.next = l2
        return result.next
