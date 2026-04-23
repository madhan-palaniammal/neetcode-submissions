# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = 0
        curr = head
        while curr:
            ln += 1
            curr = curr.next

        to_remove = ln - n
        if to_remove == 0:
            return head.next

        curr = head
        prev = ListNode()
        prev.next = curr
        while to_remove:
            to_remove -= 1
            prev = prev.next
            curr = curr.next

        prev.next = curr.next
        return head


        