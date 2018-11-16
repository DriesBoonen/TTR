# Michiel
import Speler
import TrainCards
import MissionCards
import Route

# TODO GUI triggert Beurt. Eerste keer Beurt (init): aanmaken spelers, verdelen van kaarten en aanmaken routes


class Beurt:
    id = 0 # Moet = 0 erbij? # Werkt dit? Doel is om "static variable" te hebben die hetzelfde is voor alle instanties van Beurt, zodat id altijd met 1 verhoogd kan worden.

    # Constructor
    def __init__(self, playerid): # Welke argumenten zijn het beste? Kan ik instantie van klasse Speler meegeven als argument?
        id += 1
        self.__playerid = playerid
        self.__id = id
        print(id) # For debugging purposes
        traincards = traincards()


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

        # Schudden van kaarten gebeurt in initialisatie?

        t = TrainCards.TrainCards.dealCard() # dealCard: returnt 1 kaart? Correcte methode? Instantie maken eerst?
        return t

    def conquer_route(self, routeid):
        # Code routeInnemen
        # check_completed_route == true
        # Route ergens bijhouden bij Speler of Route

    def check_completed_route(self, routeid):
        # Code controleer of er een route voltooid is
        # If (kaarten van Speler kloppen om route in te nemen en nrOfBoxes klopt)
            # Route.isTaken == true

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