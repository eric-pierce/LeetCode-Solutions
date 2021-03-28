# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = l1
        list2 = l2
        residual = 0
        answer = ListNode()
        curr_ansnode = answer
        while list1 is not None or list2 is not None or residual > 0:
            curr1 = 0
            curr2 = 0
            if list1 is not None:
                curr1 = list1.val
                list1 = list1.next
            if list2 is not None:
                curr2 = list2.val
                list2 = list2.next
            if (curr1 + curr2 + residual) > 9:
                curr_ansnode.val = (curr1 + curr2 + residual) % 10
                residual = int(((curr1 + curr2 + residual) - curr_ansnode.val) / 10)
            else:
                curr_ansnode.val = (curr1 + curr2 + residual)
                residual = 0
            if list1 is not None or list2 is not None or residual > 0:
                curr_ansnode.next = ListNode()
                curr_ansnode = curr_ansnode.next        
        return answer
