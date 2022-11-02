# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode()
        ll= dummy
        while head.next:
            if head.val == head.next.val:
                head = head.next
            else:
                ll.next = head
                ll = ll.next
                head = head.next
        ll.next = head    
        return dummy.next
                
