# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1:
            return head
        result = ListNode(0)
        gap_before = result
        gap_after = head
        gap_before.next = gap_after
        target_pointer = head
        detecting_pointer = head
        while detecting_pointer:
            tail = detecting_pointer
            for i in range(k-1):
                detecting_pointer = detecting_pointer.next
                if not detecting_pointer:
                   return result.next
            target_pointer = target_pointer.next
            for i in range(k-1):
                detecting_pointer = target_pointer.next
                gap_before.next = target_pointer
                target_pointer.next = gap_after
                gap_after = target_pointer
                target_pointer = detecting_pointer
            gap_before = tail
            gap_after = target_pointer
            gap_before.next = gap_after
        return result.next

# using tail insertion and stack are both good solutions

solution = Solution()
link = ListNode(1)
pre_node = link
pre_node.next = ListNode(2)
pre_node = pre_node.next
pre_node.next = ListNode(3)
pre_node = pre_node.next
pre_node.next = ListNode(4)
pre_node = pre_node.next
pre_node.next = ListNode(5)
# pre_node = pre_node.next
# pre_node.next = ListNode(6)
# pre_node = pre_node.next
# pre_node.next = ListNode(7)


result = solution.reverseKGroup(link,2)
while result:
    print(result.val)
    result = result.next

# #This code exchange the n and nk nodes
# class Solution(object):
#     def reverseKGroup(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         if k == 1:
#             return head
#         fast = head
#         for i in range(k-2):
#             if fast.next:
#                 fast = fast.next
#             else:
#                 break
#         if not fast.next:
#             return head
#         result = ListNode(0)
#         slow = result
#         slow.next = head
#         if k == 2:
#             while head and head.next:
#                 first_node = head
#                 second_node = head.next
#                 first_node.next = second_node.next
#                 second_node.next = first_node
#                 slow.next = second_node
#                 slow = first_node
#                 head = first_node.next
#             return result.next

#         while fast.next:
#             temp_pointer = fast.next
#             fast.next = slow.next
#             slow.next = temp_pointer
#             temp_pointer = fast.next.next
#             fast.next.next = slow.next.next
#             slow.next.next = temp_pointer
#             for i in range(k):
#                 fast = fast.next
#                 slow = slow.next
#                 if not fast.next:
#                     return result.next
#         return result.next 
