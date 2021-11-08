class NodeKth():
  def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkeKth():
  def __init__(self):
    self.headval = None

  def array(self,value):
    for i in value:
      Nodee = self.headval
      newdata = NodeKth(i)
      if Nodee is None :
        self.headval = newdata
      else:
        while Nodee.nextval :
          Nodee=Nodee.nextval
        Nodee.nextval = newdata
  def to_string(self):
        if self.headval:
            data_str = 'head -> '
            current = self.headval
            while current:
                data_str += '['+str(current.dataval)+'] -> '
                current = current.nextval
            data_str += 'x'
            return data_str


  def Kthindex(self,value):
    current=self.headval
    count =0
    while current :
      count+=1
      current = current.nextval
      k_len = count-value
    current=self.headval
    if value <0:
        print('the value is not exist')
    else:
        if k_len >=0:
            for i in range(k_len):
                value=current.dataval
                current=current.nextval
            print(value)

        else:
            print('the value is longer then array  ')

Kth = LinkeKth()
Kth.array([1,2,3,4])
Kth.Kthindex(1)
