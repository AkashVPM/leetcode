from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root == None: return []
        whole_list =[]
        level = 0

        queue = deque([root])

        while queue: 
            dummy = []
            for i in range(len(queue)): 
                current = queue.popleft()
                dummy.append(current.val)

                if current.left is not None: queue.append(current.left)
                if current.right is not None: queue.append(current.right)

            if level % 2 == 1: 
                dummy.reverse()

            whole_list.append(dummy)
            level += 1
        
        return whole_list

        