# class Node:
#   def __init__(self, value=None, next_node=None):
#     # the value at this linked list node
#     self.value = value
#     # reference to the next node in the list
#     self.next_node = next_node

#   def get_value(self):
#     return self.value

#   def get_next(self):
#     return self.next_node

#   def set_next(self, new_next):
#     # set this node's next_node reference to the passed in node
#     self.next_node = new_next

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    # pass
    self.size += 1
    self.storage.append(item)
    return self.len()
    # print(self.storage)

    # return self.size
  
  def dequeue(self):
    # pass
    if self.len() < 1:
      return None
    else:
      self.size -= 1
      return self.storage.pop(0)
      # return self.len()

  def len(self):
    # pass
    return len(self.storage)

# new_queue = Queue()
# print(new_queue.len())