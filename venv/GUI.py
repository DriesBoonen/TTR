import networkx as nx #soort van graph waar we het spelbord van kunnen maken
import Route
import Speler
import tkinter

class GUI:

    def __init__(self, board, start, score, win):
        self.__board = board
        self.__start = start

        self.__board = score
        self.__start = win


    def initgame(self, start):
        # eerst namen ingeven: spelers aanmaken dus

        selectedNames = []
        count = 0

        while count < 5:
            name = raw_input("Player "
                         + str(self.posToMove + 1)
                         + " please enter your name: (Must be unique) "
                         )
            age = raw_input("Player "
                         + str(self.posToMove + 1)
                         + " please enter your age: (Must be number) "
                         )
            count += 1

            # Beter met constructor van speler werken? ID = count (+ 1?) -> Volledige spelers doorgeven (objecten)
            # Of enkel info doorgeven en aanmaken van spelers (objecten) in constructor Beurt?
            Speler.set_age(age)
            Speler.set_name(name)
            #ook nog CPU en leeftijd: leeftijd nog in GUI en CPU-spelers aanmaken in Beurt (logica)?

            # Alle info (naam, leeftijd, kleur) doorgeven aan Beurt -> constructor Beurt maakt Speler en CPU-spelers?
    # hierna kaarten genereren? Gebeurt in Beurt
    #       in samenwerking met cards?
    # #NOTA VAN ELMER: Cards aanmaken--> self.deck = TrainCards.TrainCards() aantallen zijn reeds hardcoded (Traincards is bestand en classnaam)



    def initbord(self, board):
        self.bord = nx.Graph()
        self.cities = [
                        ]

        for city in self.cities:
            self.bord.add_node(city)


#dan iets da we kunnen laten samenwerken met route? om de edges(routes) tussen de nodes te kunnen maken