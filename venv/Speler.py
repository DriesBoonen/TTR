#import TrainCards

class Speler:
    #constructor
    def __init__(self, id, name, age, color, startHand):


        self.__id= id
        self.__name = name          #deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__age = age            #deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__color = color        #deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__pawnnr = 20
        self.__missionscomp = 0

        self.hand = collections.Counter() #klopt dit? ELMER?
                                                    #Met collection.counter is beter denk ik: card=TrainCards.dealCard();self.hand[card] += 1; maar kdenk collection best nog initialiseren
                                                    #Op die manier wordt elke kleur (dus "red" bv) als een aantal bijgehouden ipv een lijst

        missioncard1 = MissionCards.MissionCards.dealMission()
        missioncard2 = MissionCards.MissionCards.dealMission()
        player.set_currmissions((missioncard1, missioncard2))
        # moet nog geschreven worden denk ik, ELMER?
        # Wordt aan gewerkt, moet nog uitvissen hoe ik die records maak


        #dit zou dan de constructor zijn om nieuwe spelers aan te maken? 'Jaa (Dries) :D'
        #Je geeft dan id, name, age, color mee in het startscherm (GUI)  'id genereer je automatisch bij het startscherm of hier?, de rest komt uit het startscherm'

        #pawnnr, missionscomplete, traincards en missioncards worden dan gegenereerd? (controleren of dit wel de juiste instanties zijn?)



    #onderstaande is vrij overbodig denk ik

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

