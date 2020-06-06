class welt():
    def __init__(self, lootmult, monstermult, gegnerbisloot ):
        self.lootmult = lootmult
        self.monstermult = monstermult
        self.gegnerbisloot = gegnerbisloot
    #def rndgegner(self):

class wesen():
    def __init__(self, name,  asciiart):
        self.name = name
        self.asciiart = asciiart


class spieler(wesen):
    def __init__(self, name, asciiart):
        self.leben = 20
        self.maxleben = 20
        self.schaden = 10
        super().__init__( name,  asciiart)

class monster(wesen):
    def __init__(self, name, asciiart, leben, schaden):
        self.leben = leben
        self.schaden = schaden
        super().__init__(name,asciiart)

asciispieler="x["

class spiel():
    def __init__(self):
        self.eingabe ="ka lass dir was einfallen"
        self.version = 0.1
        self.credits= ("Bendix und Oscar")
    def start(self):
        self.eingabe= input("Hallo Fremder... \nWie draf ich dich nennen? \n")
        LocalSpieler=spieler(self.eingabe, asciispieler)
        self.eingabe = input()
        if self.eingabe == "1":
            print("wilkommen in der welt")
        else:
            print("Du bist im Laden")
a="xD"
Monster1 = monster("Wolf", a, 20, 1)

Session1 = spiel()
Session1.start()

