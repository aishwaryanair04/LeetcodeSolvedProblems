# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev, curr = None, slow
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        firstHalf, secondHalf = head, prev
        
        while firstHalf and secondHalf:
            if firstHalf.val != secondHalf.val:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        
        return True
            


            
            
        
        
        
        