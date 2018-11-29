class CPUSpeler(Speler):
    def __init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, isCPU, hand):
        Speler.__init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, hand)
        self.__isCPU = isCPU

        #Michiel: constructor van Speler met "super(CPUSpeler, self).__init__()"
        
        # Of def __init__(self):
        #       Speler.__init__(self, isCPU=True) # Mss wel de volgorde van argumenten omdraaien?

        # Pawn op 20 zetten, random leeftijd, namen van CPU-spelers, willekeurige missioncards en traincards trekken