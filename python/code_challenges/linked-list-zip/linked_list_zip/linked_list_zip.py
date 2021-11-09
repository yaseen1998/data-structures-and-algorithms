class NodeZip():
   def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None
class LinkedZip():
  def __init__(self):
    self.headval = None

  def Zip(self,value,value2):
    longest = len(value) if len(value)>len(value2) else len(value2)
    first = value if len(value) != 0 else value2

    for i in range(longest):
      Nodee = self.headval
      if Nodee is None :
        newdata = NodeZip(first[i])
        self.headval = newdata
        Nodee = newdata
      if i != 0 and i < len(value):
        while Nodee.nextval :
          Nodee=Nodee.nextval
        Nodee.nextval = NodeZip(value[i])
      if i < len(value2):
        while Nodee.nextval :
          Nodee=Nodee.nextval
        if len(value) == 0 and i < len(value2)-1:
            Nodee.nextval = NodeZip(value2[i+1])
        elif len(value) != 0:
            Nodee.nextval = NodeZip(value2[i])

  def to_string(self):
    if self.headval :
        data_str = 'head -> '
        current = self.headval
        while current:
            data_str += '['+str(current.dataval)+'] -> '
            current = current.nextval
        data_str += 'x'
        return data_str
    if self.headval == None:
        return('the list is empty')

ll = LinkedZip()
ll.Zip([5,6,7,8],[1,2,3,4])
print(ll.to_string())


