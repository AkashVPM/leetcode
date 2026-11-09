# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        pointer_1 = headA
        pointer_2 = headB
        count = 0

        while pointer_1 is not pointer_2:
            if pointer_1 == pointer_2: 
                return pointer_1
            
            if pointer_1 is None: 
                pointer_1 = headB
            else:
                pointer_1 = pointer_1.next

            if pointer_2 is None: 
                pointer_2 = headA
            else:
                pointer_2 = pointer_2.next
        
        return pointer_1
    
            


        