# This file will hold the building blocks for the player character and other enemies
# Might hardcode bosses at first
# Everything is just getting set up right now
class Character:
    def __init__(self, name, current_loc):
        self.name = name
        self.current_loc = current_loc

class Player:
    def __init__(self):
        pass

class AreaBoss:
    pass

class AreaEnemy:
    pass

class FinalBoss:
    pass

class DialogNPC:
    pass

class CharStats:
    def __init__(self, hp, phy, spc, wit, spd):
        self.__hp = hp
        self.__phy = phy
        self.__spc = spc
        self.__wit = wit
        self.__spd = spd
    # GET METHODS
    def getHp(self):
        return self.__hp
    def getPhy(self):
        return self.__phy
    def getSpc(self):
        return self.__spc
    def getWit(self):
        return self.__wit
    def getSpd(self):
        return self.__spd
    def getStatLine(self):
        return "Health: " + self.__hp + ", Physical: " + self.__phy + ", Special: " + self.__spc + ", Wit: " + self.__wit + ", Speed: " + self.__spd
    
    # SET METHODS
    def setHp(self, hp):
        self.__hp = self.__hp + hp
    def setPhy(self, phy):
        self.__phy = self.__phy + phy
    def setSpc(self, spc):
        self.__spc = self.__spc + spc
    def setWit(self, wit):
        self.__wit = self.__wit + wit
    def setSpd(self, spd):
        self.__spd = self.__spd + spd

