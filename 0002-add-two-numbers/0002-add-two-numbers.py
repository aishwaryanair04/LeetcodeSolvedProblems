# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = l1
        
        x = 1
        num1 = 0
        while curr:
            val = curr.val * x
            num1 += val
            x = x*10
            curr = curr.next
        
        curr = l2
        x = 1
        num2 = 0
        while curr:
            val = curr.val * x
            num2 += val
            x = x*10
            curr = curr.next
        
        result = str(num1 + num2)
        list1 = []
        for char in result:
            list1.append(int(char))
        
        
        dummy = ListNode(0)
        tail = dummy
        
        for num in list1:
            new_node = ListNode(num)
            tail.next = new_node
            tail = tail.next
        
        
        prev, curr = None, dummy.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
            
            
            
        