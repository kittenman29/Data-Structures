class Queue:
  def __init__(self, size=0, storage=[]):
    self.size = size
    # what data structure should we
    # use to store queue elements?
    self.storage = storage

  def enqueue(self, item):
    # pass
    if item is None:
      return None
    else:
      self.storage.append(item)
    return len(self.size)
  
  def dequeue(self):
    pass
    # if len(self.size) < 1:
    #   return None
    # return self.storage.pop()

  def len(self):
    pass
    # return len(self.size)
