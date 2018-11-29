# import networkx as nx #soort van graph waar we het spelbord van kunnen maken
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

                # doorgeven en ga naar beurt dan?


    def initbord(self, board):
        self.bord = nx.Graph()
        self.cities = [
                        ]

        for city in self.cities:
            self.bord.add_node(city)


#dan iets da we kunnen laten samenwerken met route? om de edges(routes) tussen de nodes te kunnen maken