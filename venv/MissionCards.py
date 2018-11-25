
import random

class MissionCards(object):

    self.missions = [(("Stad1, Stad2"), (("Tussen1, Tussen2, Tussen3"),("Tussen1, Tussen3"),("Tussen1, Tussen2, Tussen4"))),
                (("Stad2, Stad3"), (("Tussen4, Tussen5"), ("Tussen5"), ("Tussen5, Tussen6")))  #Enzovoort kunnen we deze hardcoden
               ]

    #print(missions[0][1][2])  #Dit geeft "Tussen1, Tussen2, Tussen4" uit eerste missie, op deze manier kunnen we dus wel de tuples doorzoeken ;)
                                #TUPLES ZIJN IMMUTABLE --> Onwijzigbaar na initialisatie van values!

    self.shuffle(missions)  #Schud de missies door mekaar


    def dealMission(self):
        try:
            return self.missions.pop() #Geeft de laatste item uit de list, dus dankzij shuffle een random mission
        except IndexError: #Als de stapel leeg is zullen we een IndexError krijgen en opvangen
            #SPEL STOPPEN
            print("Tis gedaan")


    #OPMERKING: Deck en Weggooistapel niet nodig omdat wij de objecten gewoon verwijderen zonder meer
    #           We staan namelijk niet toe dat er kaarten worden bijgevuld,....
    #           Hetzelfde geldt voor de traincards!