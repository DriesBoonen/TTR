# Michiel
import Speler
import CPUSpeler
import GUI
import TrainCards
import MissionCards
import Route
from random import randint
from collections import defaultdict
d = defaultdict(int)

# Iedere keer nieuwe instantie van Beurt? Of altijd de gegevens verversen?
# TODO GUI triggert Beurt. Eerste keer Beurt (init): aanmaken spelers, verdelen van kaarten en aanmaken routes

# Aantal kaarten bijhouden live bijhouden in Speler?

class Beurt:

    # Constructor
    def __init__(self, name, age, color): # Welke argumenten zijn het beste? List of array van spelers?
        # TODO aanmaken spelers, verdelen van kaarten en aanmaken routes
        # Iedere speler krijgt 2 missiekaarten en 4 treinkaarten

        # Planning: eerst gewone speler aanmaken. Dan CPU-spelers: eerst kaarten genereren, dan toekennen bij aanmaken CPU-speler




        # Menselijke speler aanmaken: heeft id = 0
        # Treinkaarten en missiekaarten op begin van spel: constructor Speler
        player = Speler.Speler.__init__(0, name, age, color, startHand) # Menselijke speler altijd ID = 0 geven

        self.deck = TrainCards.TrainCards()

        for i in range(aantalSpelers):
            for j in range(4):
                getrokkenKaart = self.deck.dealCard()
                player.addCardToHand(getrokkenKaart)


        d = {} # Dictionary

        # CPU-spelers aanmaken: 3 CPU-spelers (0, 1, 2, 3 en 4)
        for i in range(0, 3):
            # Random kaarten generen
            # Nieuwe CPU-speler aanmaken en kaarten toekennen via constructor?
            missioncard1 = MissionCards.MissionCards.dealMission()
            missioncard2 = MissionCards.MissionCards.dealMission()

            # 4 treinkaarten nemen om te starten
            for k in range(0,3):
                traincard = TrainCards.TrainCards.dealCard()
                traincards_array.append(traincard) # # Indien methode "TrainCards.dealcard" kaartenteller van Speler verhoogt, dan is dit niet nodig

            # cpu1, cpu2 en cpu3: werkt dit?
            d["cpu" + str(i+1)] = CPUSpeler.CPUSpeler.__init__(i+1, i+1, randint(10, 99), OVERIGE_KLEUREN, PAWNNR, 0, (missioncard1,missioncard2), True, ARRAY VAN AANTALLEN KAARTEN) # Willekeurige leeftijd tussen 10 en 99



    # Getters
    def get_id(self):
        return self.__id

    def get_playerid(self):
        return self.__playerid

    # Setters
    def set_id(self, newid):
        self.__id = newid

    def set_playerid(self, newplayerid):
        self.__playerid = newplayerid

    # Normal methods
    def swap_mission(self, mission_to_change):
        # Op einde: return of Speler zijn hand wijzigen?
        # mission_to_change = MissionCards.MissionCards.random
        # return missie_to_change

    def extra_traincard(self):
        # Functie extraCards(aantal kaarten die je moet bijkrijgen)
        t = TrainCards.TrainCards.dealCard() # dealCard: returnt 1 kaart? Correcte methode? Instantie maken eerst?
                                                #NOTA VAN ELMER: Best object bv "Deck" aanmaken --> self.deck = TrainCards.TrainCards()
                                                #Dit initialiseert Traincards met een stapel, daarna doe je self.deck.dealCard()" natuurlijk in de speler zijn hand
        return t

    def conquer_route(self, routeid):
        # Code routeInnemen
        # check_completed_route == true
        # Route ergens bijhouden bij Speler of Route

    def check_completed_route(self, routeid):
        # Code controleer of er een route voltooid is
        # If (kaarten van Speler kloppen om route in te nemen en nrOfBoxes klopt)
            # Route.isTaken == true




# OUDE COMMENTS
# TODO constructor van Speler: gegevens startscherm (naam, leeftijd) + kaarten genereren

# TODO eerste beurt -> init, dit gebeurt in klasse Speler
# TODO eerste beurt -> spelbord in GUI initialiseren
# TODO eerste beurt -> vanuit GUI, initBoard alle routes definieren (hardcoded) + scorebord

# TODO spel bezig:
# TODO Hoe missiekaarten controleren qua uitvoerbaarheid? Eerst knop onklikbaar zetten en op begin van beurt berekenen wat kan en wat niet kan
# TODO route innemen -> eerst op GUI route aanklikken -> naar klasse Route om info over die route op te halen -> naar Beurt -> naar Speler: controle of speler genoeg kaarten heeft -> speler geeft go of no go aan Beurt (true/false)
# TODO -> LET OP: meerdere routes tussen steden mogelijk!

# NOTE: CPU-speler -> focussen op missiekaarten (wel 2 trekken) en altijd kortste route laten nemen
# NOTE: voor routes 0 als ingenomen en 1-4 de spelers