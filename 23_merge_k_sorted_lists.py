# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # import heapq
        # result = ListNode(0)
        # pre_node = result
        # pq = []
        # for i in range(len(lists)):
        #     if lists[i]:
        #         heapq.heappush(pq,(lists[i].val,i))
        #         lists[i] = lists[i].next
        # while pq:
        #     val, index = heapq.heappop(pq)
        #     pre_node.next = ListNode(val)
        #     pre_node = pre_node.next
        #     # now we need to push the node behind the poped node to the priority queue, 
        #     # if there's no node behind then we don't need to push anything, 
        #     # it's just like transform the k-list question to a k-1 list question 
        #     if lists[index]:
        #         heapq.heappush(pq,(lists[index].val,index))
        #         lists[index] = lists[index].next
        # return result.next

        # divide and conquer
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            for i in range(len(lists)//2):
                merged_result = ListNode(0)
                pre_node = merged_result
                pointer1 = lists[i]
                pointer2 = lists[i+1]
                while pointer1 and pointer2:
                    if pointer1.val <= pointer2.val :
                        pre_node.next = pointer1
                        pointer1 = pointer1.next
                        pre_node = pre_node.next
                    else:
                        pre_node.next = pointer2
                        pointer2 = pointer2.next
                        pre_node = pre_node.next
                if pointer1:
                    pre_node.next = pointer1
                else:
                    pre_node.next = pointer2
                lists[i] = merged_result.next
                del(lists[i+1])
        return lists[0]



solution = Solution()
input_lists = []

link1 = ListNode(1)
pre = link1
pre.next = ListNode(4)
pre = pre.next
pre.next = ListNode(5)
input_lists.append(link1)

link1 = ListNode(1)
pre = link1
pre.next = ListNode(3)
pre = pre.next
pre.next = ListNode(4)
input_lists.append(link1)


link1 = ListNode(2)
pre = link1
pre.next = ListNode(6)
input_lists.append(link1)

result = solution.mergeKLists(input_lists)
print("result")
while result:
    print(result.val)
    result = result.next
                

                     