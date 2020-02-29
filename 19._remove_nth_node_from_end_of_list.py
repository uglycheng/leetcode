# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # #fast and slow pointer, fast pointer moves n step firstly. Then fast and slow move together, when fast reach the end, slow is pointing the -(n+1) node.
        # fast = head
        # slow = head
        # for i in range(n):
        #     if fast.next:
        #         fast = fast.next
        #     else:
        #         return head.next
        # while fast.next :
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head

        node_dict = {1:head}
        i = 1
        pointer = head.next
        while pointer:
            i += 1
            node_dict[i] = pointer
            pointer = pointer.next
        if i == n:
            return head.next
        node_before_deleted = node_dict[i-n]
        node_before_deleted.next = node_before_deleted.next.next
        return head
            

       