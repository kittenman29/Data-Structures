class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage) -1
    self._bubble_up(index)

  def delete(self):
    if len(self.storage) == 0:
      return
    
    end = len(self.storage) -1
    root = self.storage[0]
    end, root = root, end
    self.storage.pop()
    # print(root)
    self._sift_down(0)
   


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return
    parent = (index -1) // 2
    if self.storage[index] > self.storage[parent]:
      self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      self._bubble_up(parent)

    
  def _sift_down(self, index):
    if index >= len(self.storage) -1:
      return

    left_child = index * 2 + 1
    right_child = index * 2 + 2
    child = max(self.storage[left_child], self.storage[right_child])
    child_index = max(left_child, right_child)
    # print(child)
    print(self.storage[index])
    print(child)
    print(len(self.storage)-1)
    print(child_index)

    if self.storage[index] < child and len(self.storage)-1 > child_index:
      self.storage[index], child = child, self.storage[index]
      # print(self.storage[index])
      self._sift_down(self.storage[index])
    else:
      return 





h = Heap()
h.insert(6)
h.insert(8)
h.insert(10)
h.insert(9)
h.insert(1)
h.insert(9)
h.insert(9)
h.insert(5)
# print(h.get_max())
print(h.delete())