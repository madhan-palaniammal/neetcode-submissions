# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        proxyhead = tmp = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next

        tmp.next = list1 or list2

        return proxyhead.next

