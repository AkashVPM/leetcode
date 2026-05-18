'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count  = 0 
        current = head
        i = 1
        
        while current:
            current = current.next
            count += 1
        
        if count == n: 
            return head.next
        
        change = count - n 
        current = head

        while i < change: 
            current = current.next
            i +=  1 
        
        current.next = current.next.next
           
        return head
      
    def removeNthFromEndSinglePass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy 
        right = dummy 

        for i in range(n): 
            right = right.next 

        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next
        