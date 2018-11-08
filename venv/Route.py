class Route:
    def __init__(self, color, nrOfBoxes, city1, city2, isTaken):
        self.__color = color
        self.__nrOfBoxes = nrOfBoxes
        self.__city1 = city1
        self.__city2 = city2
        self.__isTaken = isTaken
    #
    # getters and setters
    #
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def get_nrOfBoxes(self):
        return self.__nrOfBoxes
    def set_nrOfBoxes(self, nrOfBoxes):
        self.__nrOfBoxes = nrOfBoxes

    def get_city1(self):
        return self.__city1
    def set_city1(self, city1):
        self.__city1 = city1

    def get_city2(self):
        return self.__city2
    def set_city2(self, city2):
        self.__city2 = city2

    def get_isTaken(self):
        return self.__isTaken
    def set_isTaken(self, isTaken):
        self.__isTaken = isTaken

#mkjmlk