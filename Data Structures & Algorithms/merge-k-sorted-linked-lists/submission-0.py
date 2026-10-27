# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge2Lists(left, right))
            
            lists = merged
        
        return lists[0]
    
    def merge2Lists(self, left, right):
        dummy = ListNode()
        cur = dummy

        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        
        cur.next = left if left else right
        return dummy.next
        