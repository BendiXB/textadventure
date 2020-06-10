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
  / / / _ \| |/_/ __/  / /| |/ __  / | / / _ \/ __ \/ __/ / / / ___/ _ \\
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
    shop="""    
  _____________________        __   __  _  __    _ ____
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|    
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|    [1] Ein Schwert für den Preis von 10 Gold
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |    [2] Einenen Panzer für die zarte Brust des
  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|     Kriegers für den Preis von 15 Gold
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|    [3] Eine Pilzsuppe die einen wieder auf die
  | _____   _   __  |/      \../      \|  __   __   ___|    Beine bringt für den Preis von 5 Gold
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||    [4] Die Reinigung deiner Seele für den Preis
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||    von 666 Gold
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|    [5] Einen verzierten Plattenpanzer für den 
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|    Preis von 90 Gold
  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|    
__|  \/\|/   /(____|/ //                    /  /||~|~|~|__  [6] Eine Blutspende abgeben
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|    [7] Weiter erkunden
      /                  \|________)     /  / | |   
"""

    spieler = """
        ___
     __|___|__
      ('o_o')
      _\~-~/_    ______.
     //\__/\ \ ~(_]---'
    / )O  O( .\/_)
    \ \    / \_/
    )/_|  |_\.
   // /(\/)\ \.
   /_/      \_\.
  (_||      ||_)
    \| |__| |/
     | |  | |
     | |  | |
     |_|  |_|
     /_\  /_\.
    """
    tod = """
              ___          
            /   \\\\        
       /\\\\ | . . \\\\       
     ////\\\\|     ||       
   ////   \\\\ ___//\       
  ///      \\\\      \      
 ///       |\\\\      |     
//         | \\\\  \   \    1
/          |  \\\\  \   \   
           |   \\\\ /   /   
           |    \/   /    
           |     \\\\/|     
           |      \\\\|     
           |       \\\\     
           |        |     
           |_________\  
    """
    drache = """
                        -,,,__
                     \    ``~~--,,__                /   /
                     /              ``~~--,,_     //--//
          _,,,,-----,\              ,,,,---- >   (c  c)\\
      ,;''            `\,,,,----''''   ,,-'''---/   /_ ;___        -,_
     ( ''---,;====;,----/             (-,,_____/  /'/ `;   '''''----\ `:.
     (                 '               `      (oo)/   ;~~~~~~~~~~~~~/--~
      `;_           ;    \            ;   \   `  ' ,,'
         ```-----...|     )___________|    )-----'''
                    \   /             \   \\\\
                    /  /,              `\   \\\\
                   ,'---\ \              ,---`,;,
                         ```
    """

    kaktus = """
           *-*,
       ,*\/|`| \\
       \\'  | |'| *,
        \ `| | |/ )
         | |'| , /
         |'| |, /
       __|_|_|_|__
      [___________]
       |         |
       |         |
       |         |
       |_________|
    """

    fuchs = """
              /^._
,___,--~~~~--' /'~
`~--~\ )___,)/'
    (/\\\\_  (/\\\\_
    """
    seitenumbruch = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

'''
Check Klasse
Funktionen, die humorvoll auf Datentypen prüfen
'''
class check():
    def blame(inputtocheck):
        print('Ernsthaft??')
        print(inputtocheck,' Das ist keine ordentliche Eingabe. Lern lesen...')
        return False

    def string(inputtocheck):
        if isinstance(inputtocheck, str):
            return True
        else:
            check.blame(inputtocheck)

    def intenger(inputtocheck):
        if isinstance(inputtocheck, int):
            return True
        else:
            check.blame(inputtocheck)

    def inlist(inputtocheck, list):
        if inputtocheck in str(list):
            return True
        else:
            check.blame(inputtocheck)

    def konto(Spieler, geld):
        if Spieler.geld >= geld:
            return True
        else:
            return False

class welt():
    def __init__(self,name, lootmult, monstermult, gegnerbisloot ):
        self.name = name
        self.lootmult = lootmult
        self.monstermult = monstermult
        self.gegnerbisloot = gegnerbisloot

    def weltenauswahl(liste, spieler):
        print("\n\n\n\n\n\n\n\n\n\n")
        for i in range(len(liste)):
            print("Welt [", i+1,"] ist:",liste[i].name)
            print("Die Beute wird mit ",liste[i].lootmult,"multipliziert")
            print("Dafür sind deine Feinde aber ",liste[i].monstermult,"-mal so stark.")
            print("Und du musst ",liste[i].gegnerbisloot,"-gegner Töten bis du die Beute bekommst.\n")

        x = int(input("\nin welche Welt willst du gehen?\n"))
        for i in range(len(liste))
            if i == x +1:
                liste[i].erkunden(spieler)

    def erkunden(self, spieler):
        print("Du bist im:", self.name, "\nDu musst ", self.gegnerbisloot,
              "Gegner besigen bis du den Loot bekommst.\n dafür bekommst du aber auch die ", self.lootmult,
              "fache Menge an Beute.")
        for i in range(self.gegnerbisloot):
            x = randint(1,1)
            if x == 1:
                nextgegner = Monster1
            elif x == 2:
                nextgegner = Monster2
            elif x == 3:
                nextgegner = Monster3
            elif x == 4:
                nextgegner = Monster4
            elif x == 5:
                nextgegner = Monster5

            print("Du triffst einen ", nextgegner.name, "\nWillst du wegrennen[2] oder ihn angreifen[1]\n")
            i = input()
            if i == "2":
                x = randint(1,3)
                if x == 1:
                    print("Du kannst wegrennen!! Glück gehabt!!")
                else:
                    print("Du du bist zu langsam um zu rennen der gegner holt dich ein.")
                    nextgegner.angreifen(spieler,self.monstermult)
            if i == "1":
                spieler.angreifen(nextgegner,self.monstermult)
            if spieler.gestorben == True:
                break
        if spieler.gestorben == False:
            spieler.geld = spieler.geld + (10*self.lootmult)
        elif spieler.gestorben == True:
            spieler.sterben()

class wesen():
    def __init__(self, name,  asciiart):
        self.name = name
        self.asciiart = asciiart
    def angreifen(self, gegner, monstermult):                           # Der angreifer landet den First hit
        if isinstance(self, spieler):                                   #Der spieler greift an
            gegner.leben=gegner.leben*monstermult
            gegner.schaden=gegner.schaden*monstermult
            while self.leben > 0 and gegner.leben > 0:
                gegner.leben = gegner.leben - self.schaden
                if self.leben > 0 and gegner.leben > 0:
                    self.leben = self.leben - gegner.schaden
                print(self.leben, "Leben von:", self.name, "    ", gegner.leben, "Leben von:", gegner.name)
            if self.leben <=0:
                print("Du bist gestorben")
                self.gestorben = True
                print(self.gestorben)
                gegner.reset()
            else:
                print("Du hast gewonnen")
                gegner.reset()

        elif isinstance(self, monster):                                 #Das monster greift an
            self.leben=self.leben*monstermult
            self.schaden=self.schaden*monstermult
            while self.leben > 0 and gegner.leben > 0:
                gegner.leben = gegner.leben - self.schaden
                if self.leben > 0 and gegner.leben > 0:
                    self.leben = self.leben - gegner.schaden
                print(self.leben, "Leben von:", self.name, "    ", gegner.leben, "Leben von:", gegner.name)
            print(gegner.name,self.name)
            if self.leben <= 0:
                print("Du hast gewonnen")
                self.reset()
            else:
                print("Du hast verloren")
                gegner.gestorben = True
                self.reset()
        else:
            print("Fehlermeldung! \n Das sollte nicht passieren...")

class spieler(wesen):
    def __init__(self, name, asciiart):
        self.geld = 0
        self.leben = 20
        self.maxleben = 20
        self.schaden = 10
        self.gestorben = False
        super().__init__( name,  asciiart)
    def sterben(self):                                  #nach dem Tod bekommt der Spieler eine 2te chance aber ist 20% schwächer
        self.gestorben = False
        self.leben = 20
        self.maxleben = self.maxleben*0.8
        self.schaden = self.schaden*0.8
        print("\n\n\n Du bist gestorben. Deine Eingeweide werden von einem Hobbyalchemisten aufgelesen \n und mit einer Schnecke gekreuzt. Dadurch lebst du wieder, verlierst aber 20% deiner Staerke!!\n\n\n")

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

class spiel():
    def __init__(self):
        self.lustvomspieler=1
        self.eingabe =""
        self.version = 0.1
        self.credits= ("Bendix und Oscar")
    def start(self):
        print(asciiart.title)
        self.eingabe= input("Hallo Fremder... \nWie darf ich dich nennen? \n")
        LocalSpieler=spieler(self.eingabe, asciiart.spieler)
        print("OK", LocalSpieler.name, "......\nDie Welt steht dir offen.")
        while self.lustvomspieler == 1:
            self.eingabe = input("Willst du die Welt[1] erkunden oder in den Dorfladen[2] gehen?\nOder du nimmst dir das Leben[666]\n")
            if self.eingabe == "1":
              welt.weltenauswahl(Welten,LocalSpieler)
              #World1.erkunden(LocalSpieler)
            elif self.eingabe == "2":
                self.shop(LocalSpieler)
            elif self.eingabe == "666":
                self.lustvomspieler = 4

    def shop(self,Spieler):
        print(asciiart.seitenumbruch,"Hey Hey Hey.....\n Was begiert deine Seele??")
        for i in range(200):
            print(asciiart.shop)
            print("Du hast ", Spieler.geld," Gold.")
            self.eingabe = input("\n")            print("Du triffst einen ", nextgegner.name, "\nWillst du wegrennen[2] oder ihn angreifen[1]\n")

            if self.eingabe == "1":
                if check.konto(Spieler, 10) == True:
                    Spieler.geld = Spieler.geld - 10
                    spieler.schaden = spieler.schaden + 5
                else:
                    print(
                        asciiart.seitenumbruch,"Hey Hey Hey.....\nWas begiert deine Seele??")
                    print("Du hast zu wenig Geld.")
            elif self.eingabe == "2":
                if check.konto(Spieler, 15) == True:
                    Spieler.geld = Spieler.geld - 15
                    spieler.maxleben = spieler.maxleben + 10
                else:
                    print(
                        asciiart.seitenumbruch,"Hey Hey Hey.....\nWas begiert deine seele??")
                    print("Du hast zu wenig Geld.")
            elif self.eingabe == "3":
                if check.konto(Spieler, 5) == True:
                    Spieler.geld = Spieler.geld - 5
                    spieler.leben = spieler.maxleben
                else:
                    print(
                        asciiart.seitenumbruch,"Hey Hey Hey.....\nWas begiert deine seele??")
                    print("Du hast zu wenig Geld.")
           # elif self.eingabe == "4":
                # etwas
            #elif self.eingabe == "5":
                # etwas
            #elif self.eingabe == "6":
                #etwas
            elif self.eingabe == "7":
                break
            else:
                print("Das ist leider nicht verfügbar.")

Monster1 = monster("Wolf", asciiart.wolf, 15, 10)
Monster2 = monster("Baer", asciiart.bär, 20, 8)
Monster3 = monster("Drache", asciiart.drache, 30, 20 )
Monster4 = monster("Kaktus", asciiart.kaktus, 30, 1)
Monster5 = monster("Fuchs", asciiart.fuchs, 10, 5)
World1 = welt("Wald",1,4,3)
World2 = welt("Berge",1,2,3)
World3 =  welt("Fluss", 1,2,3)
World4 = welt("Bergwerk", 1, 2,3)
World5 = welt("Hölle",10,10,10)
Welten=[World1, World2, World3, World4, World5]

Session1 = spiel()
Session1.start()