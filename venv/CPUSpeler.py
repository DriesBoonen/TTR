class CPUSpeler(Speler):
    def __init__(self, name, age, color, pawnnr, missionscomp, currmissions, isCPU):
        Speler.__init__(self, name, age, color, pawnnr, missionscomp, currmissions):
        self.__isCPU = isCPU