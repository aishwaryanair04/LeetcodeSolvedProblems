# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        tempList = []
        
        tail = head
        
        while tail:
            if tail in tempList:
                return True
            else:
                tempList.append(tail)
            tail = tail.next
        

                
        