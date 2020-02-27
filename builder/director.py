from Speaker_M import Speaker_M
from Builder import Builder

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getSpeaker(self):
        speaker_m = Speaker_M()

        power = self.__builder.getPower()
        speaker_m.setPower(power)

        
        size = self.__builder.getSize()
        speaker_m.setSize(size)

        price = self.__builder.getPrice()
        speaker_m.setPrice(price)

        producer = self.__builder.getProducer()
        speaker_m.setProducer(producer)

        return speaker_m



    