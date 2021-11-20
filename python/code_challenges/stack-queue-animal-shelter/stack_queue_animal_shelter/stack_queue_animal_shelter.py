# from stack_and_queue.node import Node
class Cat():
   def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None
    self.type='cat'

class Dog():
   def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None
    self.type='dog'

class AnimalShelter():
    def __init__(self):
        self.frontCat = None ; self.rearCat = None
        self.frontDog = None ; self.rearDog = None

    def EnQueue(self, animel):

        if animel.type=="cat":
            if self.rearCat == None:
                self.frontCat = self.rearCat = animel
                return
            self.rearCat.nextval = animel
            self.rearCat = animel
            
        if animel.type=="dog":
            if self.rearDog == None:
                self.frontDog = self.rearDog = animel
                return
            self.rearDog.nextval = animel
            self.rearDog = animel

    def DeQueue(self,value):

        if value == "cat" and self.frontCat != None :
            temp=self.frontCat
            self.frontCat=temp.nextval
            temp.nextval=None
            return temp.dataval

        elif value == "dog" and self.frontDog != None :
            temp=self.frontDog
            self.frontDog=temp.nextval
            temp.nextval=None
            return temp.dataval
        else:
            return 'null'
