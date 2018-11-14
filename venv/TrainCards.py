import random


class TrainCards:

    def __init__(self, sizeDrawPile):
        self.sizeDrawPile = sizeDrawPile
        self.colors = ["black", "white", "green", "blue", "red", "yellow"]

        #wildcards nog toevoegen
        self.cards = ["wild" for i in range(6)] + [i for i in self.possibleColors for j in range(66)]
        self.shuffle(self.cards)







    def shuffle(self, cards):
        cards:list
        random.shuffle(cards)


    def dealCard(self):

        try:
            return self.cards.pop()

        except IndexError:
            #SPEL STOPPEN
            print("Tis gedaan")


    def extraCards(self, numberOfTickets):
        numberOfTickets: int

        return(self.dealCard() for i in range(numberOfTickets))


    def cardsLeftover(self):

        return len(self.cards)

