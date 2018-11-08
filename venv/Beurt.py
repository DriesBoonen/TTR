# Michiel

class Beurt:
    id = 0 # Moet = 0 erbij? # Werkt dit? Doel is om "static variable" te hebben die hetzelfde is voor alle instanties van Beurt, zodat id altijd met 1 verhoogd kan worden.
    # Constructor
    def __init__(self, playerid): # Welke argumenten zijn het beste? Kan ik instantie van klasse Speler meegeven als argument?
        id += 1
        self.__playerid = playerid
        self.__id = id
        print(id) # For debugging purposes

    # Getters
    def get_id(self):
        return self.__id

    def get_playerid(self):
        #return self.__playerid

    # Setters
    def set_id(self, newid):
        self.__id = newid

    def set_playerid(self, newplayerid):
        self.__playerid = newplayerid

    # Normal methods
    def swap_mission(self, oldmission):
        # Code ruilMissie

    def extra_traincard(self):
        # Code extraTreinkaart

    def conquer_route(self):
        # Code routeInnemen

    def check_completed_route(self):
        # Code controleer of er een route voltooid is