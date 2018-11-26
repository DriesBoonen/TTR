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


    def start(self, start):
        # eerst namen ingeven: spelers aanmaken dus



        root = Tk()
        frame = Frame(root)
        frame.pack()

        L1 = Label(root, text="Spelernaam")
        L1.pack(side=LEFT)
        E_spelernaam = Entry(root, bd=5)
        E_spelernaam.pack(side=LEFT)

        L2 = Label(root, text="CPU1")
        L2.pack(side=LEFT)
        E_cpu1 = Entry(root, bd=5)
        E_cpu1.pack(side=LEFT)

        L3 = Label(root, text="CPU2")
        L3.pack(side=LEFT)
        E_cpu2 = Entry(root, bd=5)
        E_cpu2.pack(side=LEFT)

        L4 = Label(root, text="CPU3")
        L4.pack(side=LEFT)
        E_cpu3 = Entry(root, bd=5)
        E_cpu3.pack(side=LEFT)

        root.mainloop()


        #count = 0
        #
        # while count < 5:
        #     name = raw_input("Player "
        #                  + str(self.posToMove + 1)
        #                  + " please enter your name: (Must be unique) "
        #                  )
        #     age = raw_input("Age "
        #                  + str(self.posToMove + 1)
        #                  + " please enter your age: (Must be number) "
        #                  )
        #     count += 1






    def initbord(self, board):
        self.bord = nx.Graph()
        self.cities = [
                        ]

        for city in self.cities:
            self.bord.add_node(city)


#dan iets da we kunnen laten samenwerken met route? om de edges(routes) tussen de nodes te kunnen maken