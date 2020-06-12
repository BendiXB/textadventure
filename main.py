"""
Importe
"""
from random import *            # random wird für zufällige Spielinhalte verwendet wie die Gegnerwahl

'''
Ascii Art Klasse
Enthält Ascii Artwork strukturiert als Variablen zur verwendung in allen Teilen des Programmes
Verwendeung bsp asciiart.baer
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
    baer = '''
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
  ______________________________________________________
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|    
  || | | | | | | | | | | |/\ \  \\\\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|    [1] Ein Schwert für den Preis von 10 Gold
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\\\ /  |=|__|~|~|___| | | |    [2] Einenen Panzer für die zarte Brust des
  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|     Kriegers für den Preis von 15 Gold
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|    [3] Eine Pilzsuppe die einen wieder auf die
  | _____   _   __  |/      \../      \|  __   __   ___|    Beine bringt für den Preis von 5 Gold
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||    [4] Ein 5G-Schild für den Preis
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
//         | \\\\  \   \    
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
    welt = """
            _,--',   _._.--._____
 .--.--';_'-.', ";_      _.,-'
.'--'.  _.'    {`'-;_ .-.>.'
      '-:_      )  / `' '=.
        ) >     {_/,     /~)
        |/               `^ .'
    """
    grab = """
                 _______
           _____/      \\\\_____
          |                  ||
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
  *       | *   **    * **   |**      **
   \))ejm96/.,(//,,..,,\||(,,.,\\,.((//

    """
    seitenumbruch = 20*"\n"     #Seitenumbruch klärt das Terminalfenster wenn geprintet

'''
Check Klasse
Funktionen, die humorvoll Eingaben prüfen
'''
class check():
    # blame wird aufgerufen wenn eine Prüfung negativ ist um den Nutzer zu flamen
    def blame(inputtocheck):
        print('Ernsthaft??')
        print(inputtocheck,'ist keine ordentliche Eingabe. Lern lesen...')

    # check.string prüft auf einen String
    def string(inputtocheck):               # inputtocheck ist die Variable die auf einen Typ geprüft wird
        if isinstance(inputtocheck, str):   # isinstance gibt Wahr zurück wenn ein String
            return True                     # Ausgabe der Funktion ist wahr wenn ein String
        else:
            check.blame(inputtocheck)       # Den Spieler flamen wenn Eingabe falsch
            return False                    # Ausgabe der Funktion is Falsch wenn kein String

    # check.intenger prüft auf einen Intenger
    def intenger(inputtocheck):             # inputtocheck ist die Variable die auf einen Typ geprüft wird
        if isinstance(inputtocheck, int):   # isinstance gibt Wahr zurück wenn ein Intenger
            return True                     # Ausgabe der Funktion ist wahr wenn ein Intenger
        else:
            check.blame(inputtocheck)       # Den Spieler flamen wenn Eingabe falsch
            return False                    # Ausgabe der Funktion ist wahr wenn kein Intenger

    # check.inlist prüft ob eine Eingabe in einer Liste aus Intengern enthalten ist
    def inlist(inputtocheck, list):         # An die Funktion wird eine Liste von Intengern und die zu prüfende Eingabe übergeben
        if str(inputtocheck) in str(list):  # Wenn die Eingabe in der Liste von Möglichkeiten ist
            return True                     # Ausgabe der Funktion ist wahr wenn die Eingabe in der Liste ist
        else:
            check.blame(inputtocheck)       # Gegner flamen wenn Eingabe nicht in Liste
            return False                    # Ausgabe der Funktion ist Falsch wenn die Eingabe in der Liste ist

    # check.konto prüft ob auf dem Konto eines Spielerobjektes ein übergebener Betrag liegt
    def konto(Spieler, geld):               # An die Funktion wird ein Spielerobjekt und ein Geldbetrag übergeben
        if Spieler.geld >= geld:            # Wenn der Spieler den Geltbetrag besitzt
            return True                     # Ausgabe der Funktion ist wahr wenn der Spieler genug Geld hat
        else:
            return False                    # Ausgabe der Funktion ist falsch wenn der Spieler zu wenig Geld hat

    # check.keingeld sagt dem Spieler er hat nicht genug Geld
    def keingeld():
        print("\n !!!!!!!!Du hast zu wenig Geld.!!!!!!!!!")
        print("\n\nWas möchtest du stattdessen haben?")


"""
Die Weltenklasse enthält Attribute die das Spielgeschehen beeinflussen,
die Wahl der Welten und die Funktion Erkunden() die den Spieler auf Gegner treffen lässt.
"""
class welt():
    def __init__(self,name, lootmult, monstermult, gegnerbisloot ):         #Konstruktor einer Welt
        self.name = name                        #Name der Welt
        self.lootmult = lootmult                #Beute Multiplikator
        self.monstermult = monstermult          #Multiplikator für den Schaden und das Leben der Gegener
        self.gegnerbisloot = gegnerbisloot      #Die Anzahl der gegner die man bekämpfen muss bis man den Loot bekommt


    """ 
    Weltenauswahl ist eine Methode der Klasse Welt. Sie wird von Spiel aufgerufen
    und ist zuständig für die Auswahl der Welt.
    Ihr wird eine Liste der aktuellen Welten und der der Name des aktuellen Spielers.
    """
    def weltenauswahl(liste, spieler):
        print(asciiart.seitenumbruch)
        print(asciiart.welt)                    #asciiart der Welt
        for i in range(len(liste)):             #schleife zu auflisten aller in der Liste gespeicherten Welten
            print("Welt [", i+1,"] ist:",liste[i].name)
            print("Die Beute wird mit ",liste[i].lootmult,"multipliziert")
            print("Dafür sind deine Feinde aber ",liste[i].monstermult,"-mal so stark.")
            print("Und du musst ",liste[i].gegnerbisloot,"-gegner Töten bis du die Beute bekommst.\n")
            # Ausgabe der aller Welt Atribute

        x = int(input("\nin welche Welt willst du gehen?\n")) #Speicherung des Spielerinputs in x als int für die Weltauswahl
        check.inlist(x,[1,2,3,4,5])             #Eingabe prüfen
        for i in range(len(liste)):             #Schleife um den Spielerinput auszuwerten
            if (i+1) == x:                      #siehe doc-string
                liste[i].erkunden(spieler)      #starten der erkundenmethode der ausgewählten Welt
                break
            """
            Wenn i geht von 0 bis zu der Anzahl der Elemente (Welten) in der Liste. 
            Die Spielereigabe x geht von 1 bis zu der Anzahl der Elemente in der Liste + 1 
            weil die Eingabe erst bei 1 anfängt und nicht bei 0
            """


    """
    erkunden ist eine Methode von Welt. Sie bekommt den Spielernamen übergeben und Startet die keämpfe mit gegnern.
    """
    def erkunden(self, spieler):
        print("\nDu bist im:", self.name, "\nDu musst ", self.gegnerbisloot,
              "Gegner besigen bis du den Loot bekommst.\ndafür bekommst du aber auch die ", self.lootmult,
              "fache Menge an Beute.")                  #printet allgemeine infos für den spieler
        for i in range(self.gegnerbisloot):             #schleife für gegnerauswahl und zeuteilung eines random gegners
            x = randint(1,5)                            # random int für den Zufälligen gegner
            if x == 1:
                nextgegner = Monster1                   #next gegner wird ein Monster zugeteilt todo optimieren
            elif x == 2:
                nextgegner = Monster2
            elif x == 3:
                nextgegner = Monster3
            elif x == 4:
                nextgegner = Monster4
            elif x == 5:
                nextgegner = Monster5


            """
            gibt den Nächsten gegner aus und fragt ist für die wegrennen mechanik verantwortlich.
            Man hat eine 33% chance Wegzurennen. Wenn man es versucht und nicht schafft hat der gegner
            den ersten Schlag und nicht der spieler.
            Wenn ein kampf statfindet wir die die Methode anrgreifen von denjenigem ausgefürht
            der den ersten Schlag landet. 
            Dabei wird das "opfer" und und der gegnermult übergeben.
            """
            print("\nDu triffst einen ", nextgegner.name, "\nWillst du wegrennen[2] oder ihn angreifen[1] ?")
            i = input()
            while not check.inlist(i,[1,2]):
                i = input()
            if i == "2":
                x = randint(2,3)    #x ist ein random int von 1 bis 3
                if x == 1:          #33% chance das man es schafft
                    print("Du kannst wegrennen!! Glück gehabt!!")
                else:               #nicht geschafft
                    print("Du du bist zu langsam um zu rennen der gegner holt dich ein und du musst kämpfen aber der Gegner greift zuerst an..")
                    nextgegner.angreifen(spieler,self.monstermult)      #Nicht geschafft der gegner hat den ersten schlag
            if i == "1":            #Spieler rennt nicht weg
                spieler.angreifen(nextgegner,self.monstermult)          #Spieler greift an und hat ersten schlag
            if spieler.gestorben == True:                               #falls spieler in der welt stirbt wird die Welt abgebrochen
                break
        if spieler.gestorben == False:
            spieler.geld = spieler.geld + (10*self.lootmult)            #Loot an spieler ausschenken
        elif spieler.gestorben == True:
            spieler.sterben()                                           #spieler gestorben und aufrufen von spieler.sterben()

"""
Die Wesenklasse enthält für Spieler und Monster gleichermaßen verwendete Attribute 
und die Funktion Angreifen(), die sowol auf Monster als auch Spieler vererbt wird und die Kampfmechanik enthält.
"""
class wesen():
    def __init__(self, name,  asciiart):
        self.name = name
        self.asciiart = asciiart
    """
    Angreifen ist eine methode der Klasse Wesen welche den kampf zwischen zwei wesen abhandelt.
    Das wesen was angreifen ausführt ist immer derjenige der den ersten Schlag landet. Mit der Methode werden 
    der anzugreifende (gegner) und der monstermultiplikator. 
    """
    def angreifen(self, gegner, monstermult):                           # Der angreifer landet den First hit
        if isinstance(self, spieler):                                   # Überprüfen wer angreift hier der Spieler
            gegner.leben=gegner.leben*monstermult                       # anwenden des Monstermult.
            gegner.schaden=gegner.schaden*monstermult
            while self.leben > 0 and gegner.leben > 0:                  # abwicklung des Kampfes
                gegner.leben = gegner.leben - self.schaden              # der erste schlag
                if self.leben > 0 and gegner.leben > 0:                 # überprüfen ob der gegner schon nach einem schlag tod ist
                    self.leben = self.leben - gegner.schaden            # sonst schlag von gegner
                print(self.leben, "Leben von:", self.name, "    ", gegner.leben, "Leben von:", gegner.name)
            if self.leben <=0:                                          # Überprüfe wer gestorben ist
                print("Du bist gestorben")
                self.gestorben = True                                   # Spieler ist gestorben
                print(self.gestorben)
                gegner.reset()            # Gegner schaden und leben aus standert zurücksetzen mit der methode gegner.reset()
            else:
                print("Du hast gewonnen")
                gegner.reset()
        #Das gleiche wie oben nur das self das monster ist und gegner der spieler
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
            print("Fehlermeldung! \n Das sollte nicht passieren...") # Allgemeine fehlermeldung

"""
Die Spielerklasse enthält die für Spieler spezifischen Attribute u
nd die funktion sterben() die den Spieler sterben lässt und ihn schwächer wiederbelebt.
"""
class spieler(wesen):
    def __init__(self, name, asciiart):                #Erbt name und asciiart von Wesen
        self.geld = 0
        self.leben = 20
        self.maxleben = 20
        self.schaden = 10
        self.gestorben = False
        super().__init__( name,  asciiart)              #Erbt das von Wesen
    def sterben(self):                                  #nach dem Tod bekommt der Spieler eine 2te chance aber ist 20% schwächer
        self.gestorben = False                          # zurücksezten der Variable auf False
        self.leben = 20
        self.maxleben = self.maxleben*0.8               #Maxleb und Maxschaden um 20% schwächer machen
        self.schaden = self.schaden*0.8
        print(asciiart.seitenumbruch)
        print(asciiart.grab)
        print("\n\n\n Du bist gestorben. Deine Eingeweide werden von einem Hobbyalchemisten aufgelesen \n und mit einer Schnecke gekreuzt. Dadurch lebst du wieder, verlierst aber 20% deiner Staerke!!\n\n\n")

"""
Die Monsterklasse enthält die für Gegner spezifischen Attribute 
und die Funktion reset() die den Gegner für einen Nächsten Kampf vrbereitet.
"""
class monster(wesen):
    def __init__(self, name, asciiart, leben, schaden):#Konstruktor für ein Monster
        self.leben = leben
        self.maxleben = leben                           #Standert leben zum zurücksetzen der monster nach einem kampf
        self.schaden = schaden
        self.maxschaden=schaden                         #So wie maxleben
        super().__init__(name,asciiart)                 #erbt name und asciiart von Wesen
    def reset(self):                                    #zurücksetzen des monsteres auf standart werte nach Kampf
        self.leben=self.maxleben
        self.schaden=self.maxschaden

"""
Die Spielklasse enthält den Spielablauf und den Shop.
"""
class spiel():
    def __init__(self):
        self.lustvomspieler=1                           #Variable für die hauptschleife
        self.eingabe =""                                #Variable für die eingabe
        self.version = 1.0                              # Version für credits
        self.credits= ("Bendix und Oscar")              # Weitere creditzeile die Autoren enthält
    # Funktion wird aufgerufen wenn wenn das Spiel edgültig zu ende ist
    def ende(self):
        print(asciiart.seitenumbruch)                   # Gibt den Endbildschirm aus
        print(asciiart.tod)
        print('So wie dein Leben ist auch dieses Spiel nun zu ende. \n\n')
        print('_'*30)
        print(self.version)
        print(self.credits)
    """
    Diese Funktion enthält die Hauptschleife die den Spieler durch die Welt leitet
    Sie wird zum starten des Spieles gestartet
    """
    def start(self):
        print(asciiart.title)
        self.eingabe= input("Hey Ihr da, endlich seid ihr Wach... \nWie darf ich dich nennen?\n")      #eingabe des spielernamens
        while not check.string(self.eingabe):                                                          # Eingabe sicherhalthalber prüfen
            self.eingabe = input()
        LocalSpieler=spieler(self.eingabe, asciiart.spieler)       #der Spieler Wird erstellt
        print("OK", LocalSpieler.name, "......\nDie Welt steht dir offen.")

        """
        Hauptschleife des Spiels
        Ist sie unterbrochn ist der Spieler endgültig gestorben
        """
        while self.lustvomspieler == 1:
            self.eingabe = input("\nWillst du die Welt[1] erkunden oder in den Dorfladen[2] gehen?\nOder du nimmst dir das Leben[666]\n") # Auswahl zwischen Welt und Shop
            while not check.inlist(self.eingabe,[1,2,666]): # Eingabe prüfen
                self.eingabe = input()
            if self.eingabe == "1":
              welt.weltenauswahl(Welten,LocalSpieler)       #Die weltenauswahl wird gfestartet mit der Liste aller welten und dem Spielernamen
            elif self.eingabe == "2":
                self.shop(LocalSpieler)                     #der Shop wird geöffnet und der Spilername wird übergeben
            elif self.eingabe == "666":
                self.lustvomspieler = 666                   #der Spieler hat keine Lust mehr und die bedinung der Hauptschleife wird verändert

        # Der Spieler ist tot wenn die Schleife Unterbrochen wurde
        self.ende()
    """
    Der Shop ist eine Methode der Klasse Spiel. Bei der Ausführung muss der name des Spielers übergben werden.
    Der Shop ist ein Shop indem der Spieler dinge kaufen kann.
    """
    def shop(self,Spieler):
        print(asciiart.seitenumbruch,"Hey Hey Hey.....\n Was begiert deine Seele??")
        for i in range(200):        #Eine Schleife für den Shop (nach 200 einkäufen am stück muss dann auch schluss sein
            print(asciiart.shop)    #Darstellung der asciiart mit gegenständen und preisen
            print("Du hast ", Spieler.geld," Gold.")
            self.eingabe = input()
            while not check.inlist(self.eingabe, [1,2,3,4,5,6,7]):
                self.eingabe = input()
            if self.eingabe == "1": #Schwert                     #Auswahl des spielers finden
                if check.konto(Spieler, 10) == True:            #Konto des Spielers checken
                    Spieler.geld = Spieler.geld - 10            #Geld abziehen
                    spieler.schaden = spieler.schaden + 5       #Efekt des kaufs
                else:                                           #sonst
                    check.keingeld()                            #Aufrufen von Kein geld
            elif self.eingabe == "2":  # Panzer
                if check.konto(Spieler, 15) == True:
                    Spieler.geld = Spieler.geld - 15
                    spieler.maxleben = spieler.maxleben + 10
                else:
                    check.keingeld()
            elif self.eingabe == "3":  # Suppe
                if check.konto(Spieler, 5) == True:
                    Spieler.geld = Spieler.geld - 5
                    Spieler.leben = Spieler.maxleben
                else:
                    check.keingeld()
            elif self.eingabe == "4":  # 5G Mist
                if check.konto(Spieler, 666) == True:
                    Spieler.geld = Spieler.geld - 666
                    print("**** Herzlichen Glückwunsch du bist jetzt der stolze besitzer eines 5G-Schildes. \nDie Echsenmenschen werden dir nun nichts mehr anhaben können ****")
                else:
                    check.keingeld()
            elif self.eingabe == "5":  # Gucci Schild
                if check.konto(Spieler, 90) == True:
                    Spieler.geld = Spieler.geld - 90
                    Spieler.maxleben = Spieler.maxleben + 90
                else:
                    check.keingeld()
            elif self.eingabe == "6":  # Blut spenden
                print("Dake das du dein Blut bereitstellst")
                Spieler.leben=Spieler.leben - 1
                Spieler.geld=Spieler.geld+2
                print(Spieler.leben)
                if randint(1,20) == 14:
                    print("Die Nadel war dreckig\nUPS sorry\n\nDu stirbst leider einen qualvollen Tod mit Blutvergiftung")
                    Spieler.sterben()
                if Spieler.leben <= 0:
                    print("Du hast zuviel gespendet! DU HAST JETZT KEIN BLUT MEHR!!!!")
                    Spieler.sterben()
                    break
            elif self.eingabe == "7":  # genug Kapitalismus für heute
                break

"""
Definieren der Welten und Monster
"""
Monster1 = monster("Wolf", asciiart.wolf, 15, 10)
Monster2 = monster("Baer", asciiart.baer, 20, 8)
Monster3 = monster("Drache", asciiart.drache, 30, 20 )
Monster4 = monster("Kaktus", asciiart.kaktus, 30, 1)
Monster5 = monster("Fuchs", asciiart.fuchs, 10, 5)
World1 = welt("Wald",1,0.5,3)
World2 = welt("Berge",2,1,3)
World3 =  welt("Fluss", 3,2,3)
World4 = welt("Bergwerk", 4, 3,3)
World5 = welt("Hölle",15,4,10)
Welten=[World1, World2, World3, World4, World5]

"""
Starten des Spiels
"""
Session1 = spiel()
Session1.start()