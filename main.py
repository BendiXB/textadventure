class spiel():
    def __init__(self):
        self.eingabe = 0
        self.version = 0.1
        self.credits= ("Bendix und Oscar")
    def start(self):
        self.eingabe= input("Was willst du?")
        print(self.eingabe)
    #def shop(self):       #noch in arbeit


class welt():
    def __init__(self, lootmult, monstermult, gegnerbisloot ):
        self.lootmult = lootmult
        self.monstermult = monstermult
        self.gegnerbisloot = gegnerbisloot
    #def rndgegner(self):

class wesen():
    def __init__(self, name, leben, schaden, asciiart):
        self.name = name
        self.leben = leben
        self.schaden = schaden
        self.asciiart = asciiart




"""
class spieler():        #erbt von wesen
    def __init__(self):
        #etwas

class monster():        # erbt von wesen
    def __init__(self):
        #etwas

"""




