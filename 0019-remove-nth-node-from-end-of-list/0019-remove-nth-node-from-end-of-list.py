# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        
        return dummy.next
            
        
#         prev, curr = None, head
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
        
#         node = 1
#         tail = ListNode(0, prev)
#         print(tail)
        
#         while node <= n and tail:
#             if node == n:
#                 print("node: ",node)
#                 print(tail.val)
#                 if n == 1:
#                     tail = None
#                 else:
#                     tail.next = tail.next.next
#                 break
#             else:
#                 print("in else, ", tail.val)
#                 node += 1
#                 tail = tail.next
#                 print("2nd else: ", tail.val)

        
#         print(prev)
        
#         prev2, curr2 = None, prev
#         while curr2:
#             temp = curr2.next
#             curr2.next = prev2
#             prev2 = curr2
#             curr2 = temp
        
#         return prev2
                
            
            
            
            
            
        

            
                
                
            
        