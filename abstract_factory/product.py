import abc
class AbsProdA(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_a(self):
        pass

class ProductA1(AbsProdA):
  
    def interface_a(self):
        print("prodA1")
       

class ProductA2(AbsProdA):
   
    def interface_a(self):
        print("prodA2")

class AbsProdB(metaclass=abc.ABCMeta):
 
    def interface_b(self):
        pass 

class ProductB1(AbsProdB):
 
    def interface_b(self):
        print("prodB1")

class ProductB2(AbsProdB):
 
    def interface_b(self):
        print("prodB2")