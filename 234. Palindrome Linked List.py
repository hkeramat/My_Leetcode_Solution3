# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            fast =fast.next.next
            slow = slow.next
            
        def reverseList( slow1):
        
            prev = None
            cur = slow1
        
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                
            return prev
        
        prev = reverseList(slow)
        
        l , r = head , prev
        while r:
            if l.val != r.val:
                return False
            l ,  r = l.next , r.next
            
        
        return True
