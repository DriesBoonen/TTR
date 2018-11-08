class CPUSpeler(Speler):
    def __init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, isCPU, hand):
        Speler.__init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, hand):
        self.__isCPU = isCPU