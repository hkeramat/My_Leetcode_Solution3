# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1,l2):
        
        dummy = ListNode()
        merged_pre_head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                merged_pre_head.next = l1
                l1 = l1.next
                merged_pre_head = merged_pre_head.next
            else:
                merged_pre_head.next = l2
                l2 = l2.next
                merged_pre_head = merged_pre_head.next
        
        if l1:
            merged_pre_head.next = l1
        if l2:
            merged_pre_head.next = l2
        
