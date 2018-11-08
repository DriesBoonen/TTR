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
    def set_kleur(self, color):
        self.__color = color

    def get_aantal_valkjes(self):
        return self.__nrOfBoxes
    def set_aantal_valkjes(self, nrOfBoxes):
        self.__nrOfBoxes = nrOfBoxes

    def get_stad1(self):
        return self.__city1
    def set_stad1(self, stad1):
        self.__stad1 = stad1

    def get_stad2(self):
        return self.__city2
    def set_stad2(self, city2):
        self.__city2 = city2

    def get_inIngenomen(self):
        return self.__isTaken
    def set_inIngenomen(self, isTaken):
        self.__isTaken = isTaken

#mkjmlk