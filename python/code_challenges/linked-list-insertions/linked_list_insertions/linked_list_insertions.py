class Node():
  def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None
class LinkedList():
  def __init__(self):
    self.headval = None

  def append(self,value):
    Nodee = self.headval
    newdata = Node(value)
    if Nodee is None :
      self.headval = newdata
    else:
      while Nodee.nextval :
        Nodee=Nodee.nextval
      Nodee.nextval = newdata
  def insertafter(self,Nodee ,value):
    current = self.headval
    newdata = Node(value)
    while current is not None:
      if current.dataval == Nodee:
          break
      current = current.nextval
    newdata.nextval = current.nextval
    current.nextval= newdata


  def insertbefore(self,Nodee ,value):
    current = self.headval
    newdata = Node(value)
    if current.dataval == Nodee:

        newdata.nextval = self.headval


        self.headval = newdata
    else:
        while current is not None:
            if current.nextval.dataval == Nodee:
                break
            current = current.nextval

        newdata.nextval = current.nextval
        current.nextval = newdata

  def to_string(self):
        if self.headval:
            data_str = 'head -> '
            current = self.headval
            while current:
                data_str += '['+str(current.dataval)+'] -> '
                current = current.nextval
            data_str += 'x'
            return data_str

ll= LinkedList()
ll.append(1)
ll.append('hi')
ll.append(2)
ll.append(3)
ll.insertbefore(1,'hello')
print(ll.to_string())
