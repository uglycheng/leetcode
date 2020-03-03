# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result.next = head #this is to deal with the situation when linked list only has one node
        pre_node = result

        while head and head.next:
            first_node = head
            second_node = head.next
            first_node.next = second_node.next
            second_node.next = first_node
            pre_node.next = second_node
            pre_node = first_node
            head = first_node.next
        return result.next
