# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = slow.next
        slow.next = None
        cur = head2
        prev = None
        while cur:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode

        head2 = prev
        
        cur1 = head
        cur2 = head2
        while cur1 and cur2:
            next1 = cur1.next
            cur1.next = cur2
            cur1 = next1
            next2 = cur2.next
            cur2.next = cur1
            cur2 = next2
        
        
        