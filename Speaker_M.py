from big_builder import *


class Speaker_M:
    def __init__(self):
        self.__power = None
        self.__size = None
        self.__price = None
        self.__producer = None

    def setPower(self, power):
        self.__power = power

    def setSize(self, size):
        self.__size = size

    def setPrice(self, price):
        self.__price = price
    
    def setProducer(self, producer):
        self.__producer =  producer

    def show(self):
        print ("Power: " +str( self.__power.amount))
        print ("Size: " + str(self.__size.height))
        print ("Price: " + str(self.__price.price))
        print ("Producer: " + str(self.__producer.producer))