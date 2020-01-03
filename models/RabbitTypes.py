class RabbitTypes():

    def __init__(self, typeID, name, ABV):  # constructor
        self.__typeID = typeID
        self.__name = name
        self.__ABV = ABV

    # setters
    def setName(self, name):
        self.__name = name

    def setABV(self, ABV):
        self.__ABV = ABV

    # Getters
    def getTypeID(self):
        return self.__typeID

    def getName(self):
        return self.__name

    def getABV(self):
        return self.__ABV
