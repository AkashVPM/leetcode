from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self): 
        self.whole_list = []
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if root == None: return []
        query = deque([root])

        while query:
            dummy_list = []
            for _ in range(len(query)): 
                current = query.popleft()
                dummy_list.append(current.val)
                if current.left is not None: query.append(current.left)
                if current.right is not None: query.append(current.right)

            self.whole_list.append(dummy_list)
    
        return self.whole_list
        