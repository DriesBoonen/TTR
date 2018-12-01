import Speler
from random import randint

class CPUSpeler(Speler):
    #def __init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, isCPU, hand):
        #Speler.__init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, hand)
        #self.__isCPU = isCPU

        #Michiel: constructor van Speler met "super(CPUSpeler, self).__init__()"
        
        # Of def __init__(self):
        #       Speler.__init__(self, isCPU=True) # Mss wel de volgorde van argumenten omdraaien?

        # Pawn op 20 zetten, random leeftijd, namen van CPU-spelers, willekeurige missioncards en traincards trekken

    # Michiel constructor
    # Age niet meegeven als argument in constructor CPU-Speler
    def __init__(self, id, name, color):
        age = randint(10, 99)
        Speler.__init__(self, id, name, age, color)
        Speler.Speler.set_cpu_player(True) # Werkt dit?

    def is_cpu(self):
        return True

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
            self.__age = age

    def set_color(self, color):
            self.__color = color

    def set_pawnnr(self, pawnnr):
            self.__pawnnr = pawnnr

    def set_missionscomp(self, missionscomp):
            self.__missionscomp = missionscomp

    def set_currmissions(self, currmissions):
            self.__currmissions = currmissions