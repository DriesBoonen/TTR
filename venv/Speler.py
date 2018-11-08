class Speler:
    def __init__(self, id, name, age, color, pawnnr, missionscomp, currmissions ):
        self.__id= id
        self.__name = name
        self.__age = age
        self.__color = color
        self.__pawnnr = pawnnr
        self.__missionscomp = missionscomp
        self.__currmissions = currmissions



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
    Samenwerken met treinkaarten? 
    --> zou er ongeveer zo kunnen uitzien:
    
    #add card to hand
        def addCardToHand(self, card):
            """adds a single card to hand
            assumes card is a valid choice
            card: String
            """
            if card != None:
                self.hand[card] += 1
                
        """