# Michiel
import Speler
import CPUSpeler
import GUI
import TrainCards
import MissionCards
import Route

# Iedere keer nieuwe instantie van Beurt? Of altijd de gegevens verversen?
# TODO GUI triggert Beurt. Eerste keer Beurt (init): aanmaken spelers, verdelen van kaarten en aanmaken routes

# Aantal kaarten bijhouden live bijhouden bij speler?

class Beurt:
    # id = 0 # Moet = 0 erbij? # Werkt dit? Doel is om "static variable" te hebben die hetzelfde is voor alle instanties van Beurt, zodat id altijd met 1 verhoogd kan worden.

    # Constructor
    def __init__(self, players): # Welke argumenten zijn het beste? List of array van spelers?
        # id += 1

        # TODO aanmaken spelers, verdelen van kaarten en aanmaken routes
        # Iedere speler krijgt 2 missiekaarten en 4 treinkaarten

        # Planning: eerst gewone speler aanmaken. Dan CPU-spelers: eerst kaarten genereren, dan toekennen bij aanmaken CPU-speler

        # Speler aanmaken
        player = Speler.Speler.__init__(passed_id, name, age, color)
        # 4 treinkaarten: correcte syntax?
        i = 0
        while(i < 4)
            traincard = TrainCards.TrainCards.dealCard()


        # 2 missiekaarten: correcte syntax?
        missioncard1 = MissionCards.MissionCards.dealMission()
        missioncard2 = MissionCards.MissionCards.dealMission()
        player.set_currmissions([missioncard1, missioncard2])

        # CPU-spelers aanmaken
        while i < 5:
            # Random kaarten generen
            # Nieuwe CPU-speler aanmaken en kaarten toekennen via constructor?
            cpu_player = CPUSpeler.CPUSpeler.__init__( #ONVOLLEDIG!!!!!!! )
            i =+ 1


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
        # TODO Code ruilMissie
        # mission_to_change = MissionCards.MissionCards.random
        # return missie_to_change

    def extra_traincard(self):
        # Code extraTreinkaart
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