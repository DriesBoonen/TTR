import networkx as nx #soort van graph waar we het spelbord van kunnen maken
import Route
import Speler
from tkinter import *

class GUI:

    def __init__(self, board, start, score, win):
        self.__board = board
        self.__start = start

        self.__board = score
        self.__start = win

    def onlynum(S):
        if S in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True

        return False

    def start(self, start):
        # eerst namen ingeven: spelers aanmaken dus

        master = Tk()

        Label(master, text="Speler naam - leeftijd").grid(row=0)
        Label(master, text="CPU1 naam").grid(row=1)
        Label(master, text="CPU2 naam").grid(row=1)
        Label(master, text="CPU3 naam").grid(row=1)

        e1 = Entry(master)
        e2 = Entry(master)
        e3 = Entry(master)
        e4 = Entry(master)

        vcmd = (t3.register(onlynum), '%S')            #enkel num input
        e5 = Entry(master, validate='key', vcmd=vcmd)  #voor leeftijd

        b1 = Button(master, text="Start Spel", command=buttonstart) #als er op button gedrukt wordt dan voeren we 'buttonstart' uit

        e1.grid(row=0, column=1)
        e5.grid(row=0, column=2)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        b1.grid(row=4, column=1)

        mainloop()



    def buttonstart(self):
        # hier dan overgaan naar beurt?
        # hoe doe ik da praktisch? :D

        if len(e1.get()) == 0:
            if len(e5.get()) == 0:
                # controleren dat belangrijkste textvakken niet leeg zijn
                username = e1.get()
                age = e5.get()

                if len(e2.get()) == 0:
                    cpu1 = "Patrick"
                else:
                    cpu1 = e2.get()

                if len(e4.get()) == 0:
                    cpu2= "Staf"
                else:
                    cpu2 = e3.get()

                if len(e3.get()) == 0:
                    cpu3="Marc"
                else:
                    cpu3 = e4.get()

                # doorgeven en ga naar beurt dan? hoe doe ik da juist? :D variables zijn dan: (username, age, cpu1-3)
                # kleuren moeten hier ook nog bij
                # --> effe hardcoden denk ik


    def initbord(self, board):

        # subset van kaart
        listOfCities = [
            "Berlijn", "Wenen", "Warschau", "Kiev", "Boekarest"  # 0, 1, 2, 3, 4
        ]
        routes = []
        # Berlijn to
        # Wenen to
        routes.append(Route('yellow', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (yellow)
        routes.append(Route('red', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (red)
        # Warschau to
        routes.append(Route('blue', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (blue)
        routes.append(Route('green', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (green)
        routes.append(Route('black', 1, [listOfCities[2], listOfCities[1]], 0))  # Wenen (black)
        # Kiev to
        routes.append(Route('white', 3, [listOfCities[3], listOfCities[1]], 0))  # Wenen (white)
        routes.append(Route('yellow', 1, [listOfCities[3], listOfCities[2]], 0))  # Warschau (yellow)
        # Boekarest to
        routes.append(Route('yellow', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (yellow)
        routes.append(Route('blue', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (blue)
        routes.append(Route('red', 2, [listOfCities[4], listOfCities[3]], 0))  # Kiev (red)



        self.board = nx.Graph()

        for i in range(0, len(routes)):
          #                   # from city                # to city                  # path cost                      # color of path
          self.board.add_edge(routes[i].get_cities()[0], routes[i].get_cities()[1], weight=routes[i].get_pathCost(), edgeColors=routes[i].get_color())

        #for city in range(listOfCities):
        #    self.bord.add_node(city)

        #self.board.add_edge(listOfCities[1], listOfCities[0], weight = 1, edgeColors = ['yellow', 'red'])
        #self.board.add_edge(listOfCities[0], listOfCities[2], weight=2, edgeColors=['blue', 'green'])
        #self.board.add_edge(listOfCities[2], listOfCities[1], weight=1, edgeColors=['black'])
        #self.board.add_edge(listOfCities[3], listOfCities[1], weight=3, edgeColors=['white'])
        #self.board.add_edge(listOfCities[3], listOfCities[2], weight=1, edgeColors=['yellow'])
        #self.board.add_edge(listOfCities[4], listOfCities[1], weight=2, edgeColors=['blue', 'yellow'])
        #self.board.add_edge(listOfCities[4], listOfCities[3], weight=2, edgeColors=['red'])

#dan iets da we kunnen laten samenwerken met route? om de edges(routes) tussen de nodes te kunnen maken