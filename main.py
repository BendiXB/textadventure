from random import *

'''
Ascii Art Klasse
Enthält Ascii Artwork strukturiert als Variablen zur verwendung in allen Teilen des Programmes
Verwendeung bsp asciiart.bär
'''
class asciiart():
    title = """
  ______          __     ___       __                 __                
 /_  __/__  _  __/ /_   /   | ____/ /   _____  ____  / /___  __________ 
  / / / _ \| |/_/ __/  / /| |/ __  / | / / _ \/ __ \/ __/ / / / ___/ _ \
 / / /  __/>  </ /_   / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/
/_/  \___/_/|_|\__/  /_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/ 

    """
    wolf = """
                        ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''-'
    """
    bär = '''
  _      _                        
 : `.--.' ;              _....,_  
 .'      `.      _..--'"'       `-._
:          :_.-'"                  .`.
:  6    6  :                     :  '.;
:          :                      `..';
`: .----. :'                          ;
  `._Y _.'               '           ;
    'U'      .'          `.         ; 
       `:   ;`-..___       `.     .'`.
       _:   :  :    ```"''"'``.    `.  `.
     .'     ;..'            .'       `.'`
    `.......'              `........-'`
    '''

class welt():
    def __init__(self,name, lootmult, monstermult, gegnerbisloot ):
        self.name = name
        self.lootmult = lootmult
        self.monstermult = monstermult
        self.gegnerbisloot = gegnerbisloot
    def erkunden(self, spieler):
        print("Du bist im:", self.name, "\nDu musst ", self.gegnerbisloot,
              "Gegner besigen bis du den Loot bekommst.\n dafür bekommst du aber auch die ", self.lootmult,
              "- menge an Loot.")
        for i in range(self.gegnerbisloot):
            x = randint(1,5)
            if x == 1:
                nextgegner=Monster1
            elif x == 2:
                nextgegner=Monster2
            elif x == 3:
                nextgegner=Monster3
            elif x == 4:
                nextgegner=Monster4
            elif x == 5:
                nextgegner=Monster5

            print("Du triffst einen ", nextgegner.name, "\nWillst du wegrennen[1] oder ihn angreifen[2]\n")
            i = input()
            if i == "2":
                x = randint(1,3)
                if x == 1:
                    print("du kannst wegrennen!! glück gehabt!!")
                else:
                    print("Du du bist zu langsam um zu rennen der gegner holt dich ein")
                    nextgegner.angreifen(spieler,self.monstermult)
            if i == "1":
                spieler.angreifen(nextgegner,self.monstermult)
            if spieler.leben <=0:
                break




class wesen():
    def __init__(self, name,  asciiart):
        self.name = name
        self.asciiart = asciiart
    def angreifen(self, gegner, monstermult):                        # Der angreifer landet den First hit
        if isinstance(self, spieler):       #Der spieler greift an
            gegner.leben=gegner.leben*monstermult
            gegner.schaden=gegner.schaden*monstermult
            while self.leben > 0 and gegner.leben > 0:
                gegner.leben = gegner.leben - self.schaden
                if self.leben > 0 and gegner.leben > 0:
                    self.leben = self.leben - gegner.schaden
                print(self.leben, "Leben von:", self.name, "    ", gegner.leben, "Leben von:", gegner.name)
            if self.leben <=0:
                print("du bist gestorben")
                self.sterben()
                gegner.reset()
            else:
                print("du hast gewonnen ")
                gegner.reset()

        elif isinstance(self, monster):     #Das monster greift an
            self.leben=self.leben*monstermult
            self.schaden=self.schaden*monstermult
            while self.leben > 0 and gegner.leben > 0:
                gegner.leben = gegner.leben - self.schaden
                if self.leben > 0 and gegner.leben > 0:
                    self.leben = self.leben - gegner.schaden
                print(self.leben, "Leben von:", self.name, "    ", gegner.leben, "Leben von:", gegner.name)
            if self.leben <= 0:
                print("Du hast gewonnen")
                gegner.reset()
            else:
                print("Du hast verloren ")
                self.sterben()
                gegner.reset()
        else:
            print("fehler angreifen anfang")



class spieler(wesen):
    def __init__(self, name, asciiart):
        self.geld = 0
        self.leben = 20
        self.maxleben = 20
        self.schaden = 10
        super().__init__( name,  asciiart)
    def sterben(self):                      #nach dem tot bekommt der Spieler eine 2te chance aber ist 20% schwächer
        self.leben = 20
        self.maxleben = self.maxleben*0.8
        self.schaden = self.schaden*0.8
        print("\n\n\ndu bist gestorben deine eingeweide werden von einem hobby alchemisten aufgelesen\nund mit einer schnecke gekreuzt. Dadruch lebst du wieder, verlierst aber 20% deiner staerke!!\n\n\n")



class monster(wesen):
    def __init__(self, name, asciiart, leben, schaden):
        self.leben = leben
        self.maxleben = leben
        self.schaden = schaden
        self.maxschaden=schaden
        super().__init__(name,asciiart)
    def reset(self):
        self.leben=self.maxleben
        self.schaden=self.maxschaden



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
              World1.erkunden(LocalSpieler)
            else:
                print("Du bist im Laden")


a="xD" # placeholder ascciart

Monster1 = monster("Wolf", asciiart.wolf, 15, 10)
Monster2 = monster("Baer", asciiart.bär, 20, 8)
Monster3 = monster("Drache", a, 30, 20 )
Monster4 = monster("Kaktus", a, 30, 1)
Monster5 = monster("Fuchs", a, 10, 5)
World1= welt("Wald",1,0.3,2)


Session1 = spiel()
Session1.start()

