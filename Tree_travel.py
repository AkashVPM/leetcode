from collections import deque

class Tree: 
      def __init__(self, value=0, left =None, right=None):
          self.value = value
          self.left = left
          self.right = right

def build_tree(value):
      if value is None:
          return None
      
      root = Tree(value[0])   # pass the 1
      queue = deque([root])

      i = 1 

      while i < len(value): 
            current = queue.popleft()

            if i < len(value):
                  current.left = Tree(value[i])
                  i += 1 
                  queue.append(current.left)

            if i < len(value):
                  current.right = Tree(value[i])
                  i += 1 
                  queue.append(current.right)


      return root


class Tree_Travel:
      
      def DFS_Inorder(self, root = None): # Left Node Right
            if root is None: return None
            self.DFS_Inorder(root.left)
            print(root.value)
            self.DFS_Inorder(root.right) 
      
      def DFS_Preorder(self, root = None):  # Node Left Right
            if root is None: return None
            print(root.value)
            self.DFS_Preorder(root.left)
            self.DFS_Preorder(root.right)
      
      def DFS_Postorder(self, root = None): # left, right, Node
            if root is None: return None
            self.DFS_Postorder(root.left)
            self.DFS_Postorder(root.right)
            print(root.value)

      def BFS_LevelOrder(self, root= None): # level by level
            if root is None: return None
            queue = deque(root)

            while queue: 
                  current = queue.popleft()
                  print(current.value)
                  
                  if current.left: queue.append(current.left)
                  if current.right: queue.append(current.right)


value = [1,2,3,4,5,6,7]
root = build_tree(value)

travel = Tree_Travel()
travel.DFS_Inorder(root)