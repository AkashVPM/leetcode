from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# assume the input is [1,2,3,None,None,4,5] which represents the following binary tree:

def build_tree(value): 
      if value is None:
          return None
      
      root = TreeNode(value[0])   # pass the 1 
      queue = deque([root])    

      i = 1

      while i < len(value):
            current = queue.popleft()  # pop the root node from the queue in this case it is 1

            if i < len(value) and value[i] is not None:  # check if the left child exists here i is 1 and value[1] is 2
                current.left = TreeNode(value[i])  # create the left child node
                queue.append(current.left)  # add the left child to the queue
            
            i += 1

            if i < len(value) and value[i] is not None:  # check if the right child exists here i is 2 and value[2] is 3
                current.right = TreeNode(value[i])  # create the right child node
                queue.append(current.right)  # add the right child to the queue

            i += 1
      
      return root  # return the root of the tree 

value  = [1, 2, 3, None, None, 4, 5]
root = build_tree(value)

# tree Structure 

#         1
#      /    \
#     2      3
#    / \    / \
#   N   N  4   5
