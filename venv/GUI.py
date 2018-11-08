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
            count += 1

            Speler.set_name(name)


    # hierna kaarten genereren?
    #       in samenwerking met cards?



    def initbord(self, board):
        self.bord = nx.Graph()
        self.cities = [
                        ]

        for city in self.cities:
            self.bord.add_node(city)


#dan iets da we kunnen laten samenwerken met route? om de edges(routes) tussen de nodes te kunnen maken