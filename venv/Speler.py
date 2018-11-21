#import TrainCards

class Speler:
    #constructor
    def __init__(self, id, name, age, color):


        self.__id= id               #deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__name = name          #deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__age = age            #deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__color = color        #deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__pawnnr = 20
        self.__missionscomp = 0

        for i in range(6):
            self.__hand = [TrainCards.dealCard()] #klopt dit? ELMER?

        for i in range(2)
            self.__currmissions = [MissionCards.dealCard()] #moet nog geschreven worden denk ik, ELMER?

        #dit zou dan de constructor zijn om nieuwe spelers aan te maken?
        #Je geeft dan id, name, age, color mee in het startscherm (GUI)
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


    """"
    DIT MOET IN BEURT DENK IK? in methode 'extra_train_card'
    
    Samenwerken met treinkaarten? iets met een kaarten dek waaruit je uit kan 'trekken'
    --> zou er ongeveer zo kunnen uitzien:
    
    #add traincard to hand
        def addCardToHand(self, traincard):
            """adds a single card to hand
            assumes card is a valid choice
            card: String
            """
            if traincard != None:
                self.hand[traincard] += 1
                
        """