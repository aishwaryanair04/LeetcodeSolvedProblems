# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        head = new_list
        
        while(l1 and l2):
            if (l1.val < l2.val):
                head.next = l1
                l1 = l1.next  
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        head.next = l1 or l2
        return new_list.next
        