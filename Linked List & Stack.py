'''

Your implementation must support the following examples/test cases
s = Stack()
#Test1 checks s.is_empty()==True
s.push(1)
s.push(2)
#Test2 checks s.peek()==2
s.pop()
#Test3 checks s.peek()==1
#Test4 checks s.is_empty()==False
s.pop()
#Test5 checks s.is_empty()==True

'''

class Node:
  def __init__(self, init_data):
    self.data = init_data
    self.next = None

  def __str__(self):
    return (str(self.data))

class Stack:
  def __init__(self):
    self.top = None
  def push(self, x):
    currentnode = Node(x)
    if self.top == None:
      self.top = currentnode
    elif self.top != None:
      old_node = self.top
      self.top = currentnode
      currentnode.next = old_node

  def pop(self):
    old_top = self.top
    new_top = old_top.next
    self.top = old_top.next

  def peek(self):
    return self.top.data

  def is_empty(self):
    if self.top == None:
      return True
    else:
      return False


s = Stack()
print (s.is_empty()) #True
s.push(1)
s.push(2)
print (s.is_empty()) #False
print (s.peek()) #2
s.pop()
print(s.peek()) #1
