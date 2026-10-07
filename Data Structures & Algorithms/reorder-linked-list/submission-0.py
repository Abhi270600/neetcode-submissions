# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        p1, p2 = head, prev

        while p1 and p2:

            tmp1 = p1.next
            p1.next = p2
            p1 = tmp1

            tmp2 = p2.next
            p2.next = p1
            p2 = tmp2
