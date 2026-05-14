class ListNode:
      def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class linked_list:
      def __init__(self):
            self.head = None

      def insert(self, val):
            new_node = ListNode(val)
            if self.head is None: 
                  self.head = new_node     # self.head -----> [val, next]
                  print(new_node)
            else:
                  current = self.head      # 
                  while current.next:
                        current = current.next
                  current.next = new_node

      def print_list(self):
            current = self.head
            while current:
                  print(f"{current.val} -> ", end="")
                  current = current.next  

if __name__ == "__main__":
      linked_list1 = linked_list()
      linked_list1.insert(1)
      linked_list1.insert(2)
      linked_list1.insert(3)
      linked_list1.insert(4)
      linked_list1.insert(5)

      linked_list1.print_list()