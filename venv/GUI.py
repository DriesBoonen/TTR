import networkx as nx #soort van graph waar we het spelbord van kunnen maken

import Route
import Speler
import os
from Tkinter import *
import tkMessageBox

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class GUI:

    def start(self):

        def buttonstart():
            # hier dan overgaan naar beurt?
            # hoe doe ik da praktisch? :D

            if e1.index("end") != 0:
                if agevar.get() != 0:
                    # controleren dat belangrijkste textvakken niet leeg zijn
                    username = e1.get()
                    age = agevar.get()
                    tkMessageBox.showinfo("Hello Python", "Hello " + username + " : " + age)
                    if len(e2.get()) == 0:
                        cpu1 = "Patrick"
                    else:
                        cpu1 = e2.get()

                    if len(e4.get()) == 0:
                        cpu2 = "Staf"
                    else:
                        cpu2 = e3.get()

                    if len(e3.get()) == 0:
                        cpu3 = "Marc"
                    else:
                        cpu3 = e4.get()


                    # doorgeven en ga naar beurt dan? hoe doe ik da juist? :D variables zijn dan: (username, age, cpu1-3)
                    # kleuren moeten hier ook nog bij
                    # --> effe hardcoden denk ik

        # eerst namen ingeven: spelers aanmaken dus

        master = Tk()

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "maxresdefault.png"
        abs_file_path = os.path.join(script_dir, rel_path)

        background_image = PhotoImage(file=abs_file_path)
        background_label = Label(master, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(master, text="Speler naam - leeftijd").grid(row=0)
        Label(master, text="CPU1 naam").grid(row=1)
        Label(master, text="CPU2 naam").grid(row=2)
        Label(master, text="CPU3 naam").grid(row=3)

        e1 = Entry(master)
        e2 = Entry(master)
        e3 = Entry(master)
        e4 = Entry(master)

        ages = []

        for i in range(1, 100):
            ages.append(i)

        agevar = StringVar(master)
        drop = OptionMenu(master, agevar, *ages)

        b1 = Button(master, text="Start Spel", command=buttonstart) #als er op button gedrukt wordt dan voeren we 'buttonstart' uit

        e1.grid(row=0, column=1)
        drop.grid(row=0, column=2)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        b1.grid(row=4, column=1)

        mainloop()

    def initbord(self):

        # subset van kaart
        listOfCities = [
            "Berlijn", "Wenen", "Warschau", "Kiev", "Boekarest"  # 0, 1, 2, 3, 4
        ]
        routes = []
        # Berlijn to
        # Wenen to
        #rou = Route.Route('', 0, ["", ""], 0)
        routes.append(Route.Route('yellow', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (yellow)
        routes.append(Route.Route('red', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (red)
        # Warschau to
        routes.append(Route.Route('blue', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (blue)
        routes.append(Route.Route('green', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (green)
        routes.append(Route.Route('black', 1, [listOfCities[2], listOfCities[1]], 0))  # Wenen (black)
        # Kiev to
        routes.append(Route.Route('white', 3, [listOfCities[3], listOfCities[1]], 0))  # Wenen (white)
        routes.append(Route.Route('yellow', 1, [listOfCities[3], listOfCities[2]], 0))  # Warschau (yellow)
        # Boekarest to
        routes.append(Route.Route('yellow', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (yellow)
        routes.append(Route.Route('blue', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (blue)
        routes.append(Route.Route('red', 2, [listOfCities[4], listOfCities[3]], 0))  # Kiev (red)


        board = nx.Graph()

        #hahaha ik ben echt dom (Dries)
        for i in range(0, len(routes)):
          #                   # from city                # to city                  # path cost                      # color of path
          board.add_edge(routes[i].get_cities()[0], routes[i].get_cities()[1], weight=routes[i].get_pathCost(), edgeColors=routes[i].get_color())

        copyBoard = board.copy()

        pos = nx.spring_layout(board)
        nx.draw(board, pos)
        nx.draw_networkx_edge_labels(board, pos)
        plt.ion()
        plt.show()
        plt.pause(10)
        plt.close()
        #for city in range(listOfCities):
        #    self.bord.add_node(city)

        #self.board.add_edge(listOfCities[1], listOfCities[0], weight = 1, edgeColors = ['yellow', 'red'])
        #self.board.add_edge(listOfCities[0], listOfCities[2], weight=2, edgeColors=['blue', 'green'])
        #self.board.add_edge(listOfCities[2], listOfCities[1], weight=1, edgeColors=['black'])
        #self.board.add_edge(listOfCities[3], listOfCities[1], weight=3, edgeColors=['white'])
        #self.board.add_edge(listOfCities[3], listOfCities[2], weight=1, edgeColors=['yellow'])
        #self.board.add_edge(listOfCities[4], listOfCities[1], weight=2, edgeColors=['blue', 'yellow'])
        #self.board.add_edge(listOfCities[4], listOfCities[3], weight=2, edgeColors=['red'])


my_gui = GUI()

while True:
    my_gui.initbord()
