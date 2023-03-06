class Lengthconverter:
    def __init__(self, distance):
        self.__distance=distance

    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self,value):
        self.__distance=value
        

    
