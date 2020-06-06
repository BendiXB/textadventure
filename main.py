from random import *
class welt():
    def __init__(self,name, lootmult, monstermult, gegnerbisloot ):
        self.name = name
        self.lootmult = lootmult
        self.monstermult = monstermult
        self.gegnerbisloot = gegnerbisloot
    def erkunden(self, spieler):
        x = randint(1,5)
        if x == 1:
            nextgegner=Monster1
        elif x == 2:
            nextgegner=Monster1
        elif x == 3:
            nextgegner=Monster1
        elif x == 4:
            nextgegner=Monster1
        elif x == 5:
            nextgegner=Monster1
        print("Du triffst einen ", nextgegner.name, "\n Willst du wegrennen[1] oder ihn angreifen[2]\n")
        i = input()
        if i == "1":
            x = randint(1,2)
            if x == 1:
                print("du kannst wegrennen!! glück gehabt!!")
            else:
                print("Du du bist zu langsam um zu rennen der gegner holt dich ein")
                nextgegner.angreifen(spieler)
        if i == "2":
            spieler.angreifen(nextgegner)









class wesen():
    def __init__(self, name,  asciiart):
        self.name = name
        self.asciiart = asciiart
    def angreifen(self, gegner):                        # Der angreifer landet den First hit
        while self.leben >0 and gegner.leben >0:
            gegner.leben= gegner.leben - self.schaden
            if self.leben >0 and gegner.leben >0:
                self.leben=self.leben-gegner.schaden
            print(self.leben,gegner.leben)
        if self.leben >0:
            print(self.name, " hat gewonnen #angreifen func")
        else:
            print(gegner.name,"hat gewonnen #angreifen func")

class spieler(wesen):
    def __init__(self, name, asciiart):
        self.geld = 0
        self.leben = 20
        self.maxleben = 20
        self.schaden = 10
        super().__init__( name,  asciiart)
    def sterben(self):                      #nach dem tot bekommt der Spieler eine 2te chance aber ist 20% schwächer
        self.leben = 20
        self.maxlaben = self.maxlaben*0.8
        self.schaden = self.schaden*0.8
        print("du bist gestorben")
class monster(wesen):
    def __init__(self, name, asciiart, leben, schaden):
        self.leben = leben
        self.schaden = schaden
        super().__init__(name,asciiart)
    #def gestorben(self):

asciispieler="x["

class spiel():
    def __init__(self):
        self.lustvomspieler=1
        self.eingabe ="ka lass dir was einfallen"
        self.version = 0.1
        self.credits= ("Bendix und Oscar")
    def start(self):
        self.eingabe= input("Hallo Fremder... \nWie draf ich dich nennen? \n")
        LocalSpieler=spieler(self.eingabe, asciispieler)
        print("OK", LocalSpieler.name, "......\nDie Welt steht dir offen!!!!")
        while self.lustvomspieler == 1:
            self.eingabe = input("Willst du die Welt[1]? erkunden oder in den Dorfladen[2] gehen?\n")
            if self.eingabe == "1":
              print("wilkommen in der welt")
              World1.erkunden(LocalSpieler)
            else:
                print("Du bist im Laden")


a="xD"
Monster1 = monster("Wolf", a, 20, 1)
World1= welt("Wald",1,1,1)


Session1 = spiel()
Session1.start()

