import random


class TrainCards:

    def __init__(self):
        self.colors = ["black", "white", "green", "blue", "red", "yellow"]

        #wildcards nog toevoegen
        self.cards = ["wild" for i in range(6)] + [i for i in self.colors for j in range(66)]
        self.shuffle(self.cards)


    def shuffle(self, cards):
        random.shuffle(cards)


    def dealCard(self):

        try:
            return self.cards.pop()

        except IndexError:
            #SPEL STOPPEN
            print("Tis gedaan")


    def cardsLeftover(self):

        return len(self.cards)

