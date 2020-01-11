class helmet:
    def __init__(self,color="red",size="M"):
        self.color=color
        self.size=size
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
    def getSize(self):
        return self.size
    def setSize(self,size):
        self.size=size
    def features(self):
        print("Цвет шлема: "+self.color)
        print("Размер шлема: "+self.size)
class kneePads:
    def __init__(self, color="black",size="M"):
        self.color=color
        self.size=size
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
    def getSize(self):
        return self.size
    def setSize(self,size):
        self.size=size
    def features(self):
        print("Цвет наколенников: "+self.color)
        print("Размер наколенников: "+self.size)
class elbowPads:
    def __init__(self, color="grey",size="M"):
        self.color=color
        self.size=size
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
    def getSize(self):
        return self.size
    def setSize(self,size):
        self.size=size
    def features(self):
        print("Цвет налокотников: "+self.color)
        print("Размер налокотников: "+self.size)
class equipment:
    def __init__(self,helm,kneePads,elbowPads):
        self.helmet=helm
        self.kneePads=kneePads
        self.elbowPads=elbowPads
    def setHelmet(self,helmet):
        self.helmet=helmet
    def setKneePads(self,kneePads):
        self.kneePads=kneePads
    def setElbowPads(self,elbowPads):
        self.elbowPads=elbowPads
    def features(self):
        self.helmet.features()
        self.kneePads.features()
        self.elbowPads.features()
H=helmet()
K=kneePads()
E=elbowPads()
equip=equipment(H,K,E)
equip.features()
