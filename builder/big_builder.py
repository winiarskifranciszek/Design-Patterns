from Builder import Builder
from speaker import *


class BigBuilder(Builder):
    def getPower(self):
        power = Power()
        power.amount = 500
        return power
    
    def getSize(self):
        size = Size()
        size.height= 400
        #size.width = 500
        return size

    def getPrice(self):
        price = Price()
        price.price = 500
        return price

    def getProducer(self):
        producer = Producer()
        producer.producer = "LG"
        return producer