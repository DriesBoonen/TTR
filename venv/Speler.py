#import traincard

class Speler:
    def __init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, hand ):
        self.__id= id
        self.__name = name
        self.__age = age
        self.__color = color
        self.__pawnnr = pawnnr
        self.__missionscomp = missionscomp
        self.__currmissions = currmissions

        self.__hand = hand

        self.missionscomp = 0;

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