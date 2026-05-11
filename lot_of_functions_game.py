import time
import sys
import random

def haendler_upgrade(goldbeutel, spielerHP, spielerMaxHP, spielerStr, spielerVer, mana, maxmana, trank):
   
    waren = {
        "1": {"Name": "Oger-Protein", "Preis": 20, "Effekt": "Str", "Wert": 3, "Info": "+3 Stärke"}, #ist ein dictionary keyword > schlüssel(wert) geschweifte klammmern benutzen {}
        "2": {"Name": "Stahlplatte", "Preis": 25, "Effekt": "Ver", "Wert": 2, "Info": "+2 Verteidigung"},
        "3": {"Name": "Manakristall", "Preis": 15, "Effekt": "Mana", "Wert": 5, "Info": "+5 Max Mana"},
        "4": {"Name": "Lebenselixier", "Preis": 30, "Effekt": "HP", "Wert": 50, "Info": "+20 Max HP"},
        "5": {"Name": "Heiltrank", "Preis": 10, "Effekt": "Trank", "Wert": 1, "Info": "+1 Trank-Ladung"}
    }

    print("\n--- DER HÄNDLER ---")
    print(f"Gold: {goldbeutel} | HP: {spielerHP}/{spielerMaxHP} | Str: {spielerStr} | Ver: {spielerVer} | Mana: {mana}/{maxmana} | Tränke: {trank}")
    
    while True:
        print("\nVerfügbare Upgrades:")
        for k, v in waren.items():
            print(f"{k}) {v['Name']} - {v['Preis']} Gold ({v['Info']})") # k für key v für Value / nur zur ausgabe der optionen /k und v sind konventionen kann beliebig geändert werden
        print("0 Verlassen")

        wahl = input("\nWas möchtest du kaufen? ")

        if wahl == "0":
            break
        
        if wahl in waren:
            item = waren[wahl]
            if goldbeutel >= item["Preis"]:
                # Gold abziehen
                goldbeutel -= item["Preis"]
                
                # Stats verbessern
                if item["Effekt"] == "Str":
                    spielerStr += item["Wert"]
                elif item["Effekt"] == "Ver":
                    spielerVer += item["Wert"]
                elif item["Effekt"] == "Mana":
                    maxmana += item["Wert"]
                    mana += item["Wert"] # Füllt Mana direkt mit auf
                elif item["Effekt"] == "HP":
                    spielerMaxHP += item["Wert"]
                    spielerHP += item["Wert"] # Heilt um den Betrag
                elif item["Effekt"] == "Trank":
                    trank += item["Wert"]
                
                print(f"\nErfolgreich gekauft! {item['Info']}.")
                print(f"Neues Gold: {goldbeutel}")
            else:
                print("\nDu hast nicht genug Gold!")
        else:
            print("\nUngültige Wahl.")


    return goldbeutel, spielerHP, spielerMaxHP, spielerStr, spielerVer, mana, maxmana, trank


def torwaechter_raetsel(spielerHP):
    print("Ein steinerner Torwächter erwacht...")
    time.sleep(2)
    print('"Nur wer die Wahrheit erkennt, darf passieren."')
    time.sleep(2)

    versuche = 3

    while versuche > 0:
        punkte = 0
        print("\nDer Wächter stellt dir drei Fragen:")

        antwort = input("1) Herscht hier ein Diktator (ja/nein) ").lower()
        if antwort == "ja":
            punkte += 1

        antwort = input("2) Ist der Mars größer als der Merkur (ja/nein) ").lower()
        if antwort == "ja":
            punkte += 1

        antwort = input("3) Gibt es hier Demokratie (ja/nein) ").lower()
        if antwort == "nein":
            punkte += 1

        print('\nDu hast ',punkte,' von 3 Fragen richtig.')

        if punkte >= 3:
            print("Der Torwächter nickt langsam.")
            time.sleep(2)
            print(">> Das Tor öffnet sich knarrend <<")
            return spielerHP, True   

        else:
            versuche -= 1
            spielerHP -= 10
            print("Der Wächter schlägt mit seiner Axt auf den Boden!")
            print("Du verlierst 10 HP.")
            print("Verbleibende Versuche:", versuche)
            print("Deine HP:", spielerHP)

            if spielerHP <= 0:
                print("Du bist deinen Verletzungen erlegen...")
                return spielerHP, False

    print("Der Torwächter bleibt regungslos. Das Tor bleibt verschlossen.")
    return spielerHP, False
def resetVerAng(maxspielervert,maxspielerstr):
    spielerStr = maxspielerstr
    spielerVer = maxspielervert
    return spielerVer,spielerStr


karte = [
    ["E", ".", "S", "S",'G','S'],
    ["G", "X", ".", "X",'.','X' ],
    [".", "G", "S", ".",'G','X'],
    ["X", ".", "G", "A",'.','S'],
    ["S", ".", 'X','.', "S",'G']
]
karte2 = [
    ["E", "S", "X", "S",'G','S'],
    ["X", "S", "H", "X",'.','X' ],
    ["G", "S", "S", ".",'X','X'],
    ["X", "G", "G", "X",'.','.'],
    ["S", "B", 'X','.', "S",'S']
]

besucht2 = [
    [False, False, False, False,False,False],      #alles for auf False damit bei eintritt auf True gesetzt werden kann
    [False, False, False, False,False,False],
    [False, False, False, False,False,False],
    [False, False, False, False,False,False],   
    [False, False, False, False,False,False]    
]

besucht = [
    [False, False, False, False,False,False],      #alles for auf False damit bei eintritt auf True gesetzt werden kann
    [False, False, False, False,False,False],
    [False, False, False, False,False,False],
    [False, False, False, False,False,False],   
    [False, False, False, False,False,False]    
]

def bewege_spieler(spieler_pos, richtung, karte):
    x, y = spieler_pos # entpackung des Tulpes spieler_pos =(0,0) , das Tulpel bleibt unverändert wir arbeiten stattdessen mit neuen Variable x = 0 ,y =0

    if richtung == "w":   # hoch  #richtung ist von vorheriger Usereingabe
        y -= 1
    elif richtung == "s": # runter
        y += 1
    elif richtung == "a": # links
        x -= 1
    elif richtung == "d": # rechts
        x += 1
    else:
        print("Ungültige Eingabe!") # damit keine systemabstürtze vorkommen
        return spieler_pos

    if 0 <= y < len(karte) and 0 <= x < len(karte[0]): #grenzt begehbaren weg ab
        return (x, y)
    else:
        print("Hier ist eine Wand!")
        return spieler_pos

def raum_betreten(spieler_pos, besucht):
    x, y = spieler_pos #angabe position des Spielers
    besucht[y][x] = True # setzt das kartenfel von false auf true
    return besucht[y][x]
    
        
def karte_anzeigen(karte, besucht, spieler_pos):
    print("\n Dungeon-Karte")

    for y in range(len(karte)):   # kein index da hier die zeilen gezählt werden / ähnlich wie bei den arrays in pascal
        for x in range(len(karte[0])): #Idex 0 um die breite der Karte zu nutzen
            if (x, y) == spieler_pos:
                print("P", end=" ") # Spieler momentaner Ort wir angezeigt
            elif besucht[y][x]: # wenn koordinate besucht[]
                print(karte[y][x], end=" ") # druckt offen gelegte 'Räume' 
            else:
                print("?", end=" ")   # wenn noch nicht endtdeckt
        print()
    #geht alle felder durch

        
    
    
        
    

    return

def platz(Zeile):
    time.sleep(1)
    for i in range(Zeile):
        print('')

def recover(spielerMaxHP,maxmana):
    spielerHP = spielerMaxHP
    mana = maxmana
    print('-----------------------')
    print('Du hast dich auskuriert') 
    print('-----------------------')
    time.sleep(2)
    return spielerHP,mana   

def goldstand(goldbeutel):
    zufallsgold = random.randint(5,10)
    goldbeutel = goldbeutel + zufallsgold
    print('Du erhälst',zufallsgold,'Gold!')
    print('Goldbeutel:',goldbeutel)
    return goldbeutel
    


def Schaden(DMG,KRIT,ARMOR,nextATT):
    if isinstance(DMG, tuple):
        DMG = DMG[0] 
    
    if nextATT > 0:
        print('Dein Überraschungsangriff aus der Verstohlenheit ignoriert die Rüstung des Gegners')
        DMG = DMG * 1.5
        nextATT -= 1


    elif KRIT == 0:
        DMG = DMG * 2 - ARMOR
        print('Verursachst kritischen Schaden')
    else:
        DMG = DMG - ARMOR

    zwischen = DMG - KRIT
    if zwischen <= 0:
        endschaden = 0
    else:
        endschaden = zwischen


    return  endschaden , nextATT            
        


def RüstungMinus(KRIT,ARMOR):
    if KRIT == 0:
        ARMOR = ARMOR / 3
        print('Der Zauber trifft Kritisch, u machst den Gegner richig nackig')
    else:
        ARMOR = ARMOR / 2
        print('Der Zauber trifft')


    return  ARMOR

      


def Feuerball(DMG,KRIT,ARMOR):
    if isinstance(DMG, tuple):
        DMG = DMG[0] 
    
    if KRIT == 0:
        DMG = DMG * 10 - ARMOR
        print('Der Feuerball trifft voll ins Schwarze')
    else:
        DMG = DMG + 5 - ARMOR
        print('Der Feuerball Trifft')

    zwischen = DMG - KRIT
    if zwischen <= 0:
        endschaden = 0
    else:
        endschaden = zwischen

    return  endschaden             



def Eis(KRIT):
    if KRIT == 0:
        STOP = 3
        print('Die Vereisung trifft kritisch, du gibtst dem Gegner einenen Pyjama, den der Gegner macht 3 Runden lang einen Winterschlaf')
    else:
        STOP = 2   
        print('Der Gegner ist erfolgreich für eine Runde eingefroren') 

    return STOP   




def Block(KRIT,ARMOR,schutz):
    if KRIT == 0:
        vert = ARMOR * 3
        schutz += 2
        print('Du wirst für 2 Runden blocken, kritischer BLOCK')

    else:
        vert = ARMOR * 2    
        schutz += 2
        print('Du wirst für 2 Runden blocken')

    return  vert,schutz
        


def trankHeal(HP,HPmax):
    heal = HPmax / 2
    healdanach = HP + heal
    print('Healdanach:',healdanach)
    if healdanach > HPmax:
        HP = HPmax
        
    else:
        HP = healdanach    
    print('Du heilst dich um 50 % , deiner MaxHp\n')
    print('Du hast nun',HP,'HP')
    
    
    return HP   

def pfeilhagel(DMG,ARMOR):
    if isinstance(DMG, tuple):
        DMG = DMG[0] 
    
    schaden = 0
    print('Du feuerst 10 Pfeile in die Luft Richtung Gegner')
    getroffen = 0
    for x in range(1,10):
        treffer = random.randint(1,2)
        if treffer == 1:
            getroffen += 1 
    schaden = (DMG/3) * getroffen - ARMOR
    print('Der Pfeilhagel trifft mit',getroffen,'Pfeilen')
    return  schaden 
            
            






def KritShot (DMG,ARMOR):
    if isinstance(DMG, tuple):
        DMG = DMG[0] 
    
    schaden = 0
    print('Du Zielst dem Gegner direkt ins Gesicht')
    print('Der Pfeil Trifft garantiert kritisch !')
    schaden = DMG *3 - ARMOR
    print('Du verursachst',schaden,'beim Gegener')
    return schaden


def salve(DMG, KRIT, ARMOR):
    pfeile = []
    schaden = 0  
    print('Du verschießt eine Salve von 3 Pfeilen')
    if isinstance(DMG, tuple):
        DMG = DMG[0] 
    
    for x in range(3):
        if KRIT == 0:
            print('Die Salve hat Pfeffer und trifft kritisch')
            multiplikator = random.uniform(2, 2.5)
        else:
            multiplikator = random.uniform(1, 1.5) 
            
        aktueller_pfeil = DMG * multiplikator 
        aktueller_pfeil -= ARMOR
        
        # Sicherstellen, dass kein negativer Schaden entsteht
        if aktueller_pfeil < 0: aktueller_pfeil = 0
        
        pfeile.append(aktueller_pfeil) 
        schaden += aktueller_pfeil     
        
        time.sleep(1)
        print(f'Pfeil {x+1} verursacht Schaden: {aktueller_pfeil}')

    return schaden




def unsichtbarkeit(DMG,KRIT,ARMOR):
    
    if KRIT == 0:
        sneak = DMG * 3 - ARMOR
    else:
        sneak = DMG * 2 - ARMOR
    return sneak


def armorUP(SpielerRüstung,KRIT):
    print('Du redes wie ein Löwe und buffst dadurch deine Verteidigung')
    if KRIT == 0:
         RüstungN = SpielerRüstung * 1.5
         print('Du hast gedichtet wie Goethe und hast nun',RüstungN,'Verteidgung, deine Verteidigung ist nun dichter als ein DICHTER')
    else:
         RüstungN = SpielerRüstung *1.2
         print('Aus deinen enlosen Wortdurchfall erhälst du nun eine neue Verteidigung:',RüstungN)    
    return RüstungN    



def gift(DMG,Giftdauer):
    if isinstance(DMG, tuple):
        DMG = DMG[0] 
    
    schaden = DMG * 0.5
    Giftdauer = Giftdauer + 5
    return schaden, Giftdauer



def dolchwurf(DMG,KRIT,ARMOR): 
    if isinstance(DMG, tuple):
        DMG = DMG[0] 
    
    if KRIT == 0:
        schaden = DMG *2.5-ARMOR
        rüstungM = ARMOR - DMG * 0.75
        print('Du hast kritisch getroffen, du hast die Rüstung des gegner reduziert auf',rüstungM)
    else:
        schaden = DMG *1.75-ARMOR
        rüstungM = ARMOR - DMG * 0.5
        print('Du hast getroffen, du hast die Rüstung des gegner reduziert auf',rüstungM)

    return schaden, rüstungM

def kampfrunde(Krieger,Magier,Schütze,Assasine,trank,Mana,MaxMana,DMG,SpielerHP,SpielerMaxHP,SpielerRüstung,GegnerHP,GegnerRüstung,GegnerDMG,Giftdauer,Giftschaden,blocken,schutz,gefroren,Sneakschaden,ausweichen,nextAtt,runde,win):
    statuseffekte = []
    statusSpieler = []
    print('Gegnerwerte            |             Spielerwerte')        
    print('HP:',GegnerHP,'                             HP:',SpielerHP)
    print('Verteidigung:',GegnerRüstung,'               Verteidigung:',SpielerRüstung)
    print('Mana:',Mana,'                                   Mana:',Mana)
    print('Angriff:',GegnerDMG, '                        Angriff:',DMG)
    print('Status :',statuseffekte,'                            Status:',statusSpieler)
    print('Tränke des Spielers:',trank)
    while SpielerHP > 0 and GegnerHP >0:
        if Mana < MaxMana:
             print('Du erhälst ein Mana zurück')    
             Mana += 1
             print('Mana:',Mana)    
          
        elif MaxMana < Mana:
             Mana = MaxMana                          
                
       
            
        #krieger,magier,schütze,assasine,Trank,Mana,Maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,blocken)       
        
 
        print('Runde:',runde)      
        runde += 1               
        (Krieger,Magier,Schütze,Assasine,trank,  # Wenn du etwas ändern willst, musst du es zurückgeben und auch wieder annehmen.
        Mana,MaxMana,DMG,
        SpielerHP,SpielerMaxHP,SpielerRüstung,
        GegnerHP,GegnerRüstung,GegnerDMG,
        Giftdauer,Giftschaden,
        blocken,schutz,gefroren,Sneakschaden,
        ausweichen,nextAtt,runde,win) = optionen(
        Krieger,Magier,Schütze,Assasine,trank,
        Mana,MaxMana,DMG,
        SpielerHP,SpielerMaxHP,SpielerRüstung,
        GegnerHP,GegnerRüstung,GegnerDMG,
        Giftdauer,Giftschaden,
        blocken,schutz,gefroren,Sneakschaden,
        ausweichen,nextAtt,runde,win)
 
        time.sleep(2)
        
        if Giftdauer > 0:
            GegnerHP = GegnerHP - Giftschaden
            Giftdauer -= 1
            print('Der Gegner erhält Giftschaden',Giftschaden,'noch',Giftdauer,'Runden')
            print('GegnerHP:')

        if GegnerHP > 0:
            krit = random.randint(0,5)
            if gefroren > 0:
                print('Der Gegner kann sich nicht bewegen, Er ist noch gefroren')
                time.sleep(1)
                gefroren -= 1
            elif schutz > 0:
                    if krit == 0:
                        schaden,nextAtt = Schaden(GegnerDMG,krit,SpielerRüstung,0)       
                        dmg = schaden - blocken
                        currentspielerHP = SpielerHP
                        SpielerHP = SpielerHP - dmg
                        if SpielerHP > currentspielerHP:
                            SpielerHP = currentspielerHP

                        print('Der Gegner haut ordentlich zu Trifft kritisch,aber du blockst',blocken,'Schaden')
                        print('Schaden :',schaden,'SpielerHP:',SpielerHP)
                        print('')
                        schutz -= 1
                        time.sleep(1)
                    elif krit == 1 or krit == 2 or krit == 3 or krit == 4 or krit == 5:
                        print('Der Gegner Schlägt zu!!')
                        schaden,nextAtt = Schaden(GegnerDMG,krit,SpielerRüstung,0)        
                        dmg = schaden - blocken
                        currentspielerHP = SpielerHP
                        SpielerHP = SpielerHP - dmg
                        if SpielerHP > currentspielerHP:
                            SpielerHP = currentspielerHP
                        print('Du blockst',blocken,'Schaden')
                        print('Schaden :',schaden,'SpielerHP:',SpielerHP)
                        schutz -= 1
                        print('')
                        time.sleep(2)
            elif ausweichen == True:
                trefferchance = random.randint(0,2)
                if trefferchance == 0:
                    if krit == 0:
                        schaden,nextAtt = Schaden(GegnerDMG,krit,SpielerRüstung,0)           
                        dmg = SpielerHP - schaden
                        SpielerHP = dmg
                        print('Der Gegner sieht dich nicht und tifft dich aus Glück, der Gegner haut ordentlich zu es Trifft kritisch')
                        print('Schaden :',schaden,'SpielerHP:',SpielerHP)
                        print('')
                        time.sleep(2)
                        ausweichen = False
                    else:
                        print('Der Gegner Schlägt zu!!')
                        schaden,nextAtt = Schaden(GegnerDMG,krit,SpielerRüstung,0)           
                        dmg = SpielerHP - schaden
                        SpielerHP = dmg
                        print('Schaden :',schaden,'SpielerHP:',SpielerHP)
                        print('')                   
                        time.sleep(2)
                        ausweichen = False
                else:
                    print('Du hast Glück der Gegner haut zwar um sich trifft aber nicht')    
                    ausweichen = False   
            elif krit == 0:
                    schaden,nextAtt = Schaden(GegnerDMG,krit,SpielerRüstung,0)           
                    dmg = SpielerHP - schaden
                    SpielerHP = dmg
                    print('Der Gegner haut ordentlich zu es Trifft kritisch')
                    print('Schaden :',schaden,'SpielerHP:',SpielerHP)
                    print('')
                    time.sleep(2)
            else:
                    print('Der Gegner Schlägt zu!!')
                    schaden, nextAtt = Schaden(GegnerDMG,krit,SpielerRüstung,0)           
                    dmg = SpielerHP - schaden
                    SpielerHP = dmg
                    print('Schaden :',schaden,'SpielerHP:',SpielerHP)
                    print('')
                    time.sleep(2)   
        if gefroren > 0:
            statuseffekte.append('Gefroren')
        elif gefroren == 0:
            if 'Gefroren' in statuseffekte:
                statuseffekte.remove('Gefroren')

        if Giftdauer >0:
            statuseffekte.append('Vergiftet')
        elif Giftdauer == 0:
            if 'Vergiftet' in statuseffekte:
                statuseffekte.remove('Vergiftet')   

        if ausweichen == True:
            statusSpieler.append('Unsichtbar')
        elif ausweichen == False:
            if 'Unsichtbar' in statusSpieler:
                statusSpieler.remove('Unsichtbar')  
        
        print('Gegnerwerte            |             Spielerwerte')        
        print('HP:',GegnerHP,'                             HP:',SpielerHP)
        print('Verteidigung:',GegnerRüstung,'               Verteidigung:',SpielerRüstung)
        print('Mana:',Mana,'                                   Mana:',Mana)
        print('Angriff:',GegnerDMG, '                        Angriff:',DMG)
        print('Status :',statuseffekte,'                            Status:',statusSpieler)
        print('Tränke des Spielers:',trank)
        platz(3)
        time.sleep(2)                   

        
    if SpielerHP <= 0:
        print('GAME OVER') 
    elif GegnerHP <= 0:
        print('Du hast gewonnen')
        SpielerHp = SpielerMaxHP
        Mana = MaxMana
        win = True
        runde = 1
                   

                        
            



    
      
        
    
    runde = runde + 1
    time.sleep(2)

    return Krieger,Magier,Schütze,Assasine,trank,Mana,MaxMana,DMG,SpielerHP,SpielerMaxHP,SpielerRüstung,GegnerHP,GegnerRüstung,GegnerDMG,Giftdauer,Giftschaden,blocken,schutz,gefroren,Sneakschaden,ausweichen,nextAtt,runde,win      
                    








def optionen(Krieger,Magier,Schütze,Assasine,trank,Mana,MaxMana,DMG,SpielerHP,SpielerMaxHP,SpielerRüstung,GegnerHP,GegnerRüstung,GegnerDMG,Giftdauer,Giftschaden,blocken,schutz,gefroren,Sneakschaden,ausweichen,nextAtt,runde,win):
    auswahl = True
    while auswahl == True:
        if Krieger == 1:
            print('Das sind deine Optionen:')
            print('option 1: Angriff')
            print('option 2: Blocken')
            print('Option 3: ArmorUp Mana kosten 2')
            print('option 4: Heiltrank Stück;',trank)
            ant = int(input('Du willst 1 , 2 oder 3 ?\n'))
            Krit = random.randint(0,3)
            if ant == 1:
                schadengegner,nextAtt = Schaden(DMG,Krit,GegnerRüstung,nextAtt)
                GegnerHP = GegnerHP - schadengegner
                print('Du hast den Feind',schadengegner,'Schaden verursacht, er hat nun noch',GegnerHP,'HP')
                auswahl = False
            elif ant == 2:
                print('Du wirst den nächsten Angriffs des Gegner so gut blocken wie du kannst')
                blocken,schutz = Block(Krit,SpielerRüstung,schutz)
                auswahl = False
            elif ant == 3 and Mana >= 2:
                Armored = armorUP(SpielerRüstung,Krit)
                SpielerRüstung = Armored
                Mana -= 2
                auswahl = False
            elif ant == 3 and Mana <= 2:
                print('Du hast nicht genug Mana')
                continue
            elif ant == 4:
                HP = trankHeal(SpielerHP,SpielerMaxHP)
                SpielerHP = HP
                auswahl = False
                trank -= 1
            elif ant == 5 and trank <=0:
                print('Du hast keine Tränke mehr')    
                continue
                                

        if Magier == 1:
            print('Das sind deine Optionen:')
            print('option 1: Angriff')
            print('option 2: Feuerball Mana Kosten 5')
            print('option 3: RüstungMinus Mana Kosten 10')
            print('option 4: Eis Mana Kosten 6 ')
            print('option 5: Heiltrank Stück;',trank)
            ant = int(input('Du willst 1 , 2 ,3 , 4, 5 ?\n'))
            Krit = random.randint(0,3)
            if ant == 1:
                schadengegner,nextAtt = Schaden(DMG,Krit,GegnerRüstung,nextAtt)
                GegnerHP = GegnerHP - schadengegner
                print('Du hast den Feind',schadengegner,'Schaden verursacht, er hat nun noch',GegnerHP,'HP')
                auswahl = False
            elif ant == 2 and Mana >= 5:
                print('Du setzt einen Feuerball ein und wirfst ihn richtig Gegner')
                schaden = Feuerball(DMG,Krit,GegnerRüstung)
                GegnerHP = GegnerHP - schaden
                print('Der Gegner erhält',schaden,'Schaden und qualmt ein bisschen wie Malboro Gold')
                print('Hp des Gegners:',GegnerHP)
                Mana -= 5 
                auswahl = False
            elif ant == 2 and Mana < 5:
                print('Du hast nicht genug Mana')
                continue    
            elif  ant == 3 and Mana >= 10:
                GegnerRüstung = RüstungMinus(Krit,GegnerRüstung)
                print('Der Gegner hat nun nur noch',GegnerRüstung,'Rüstung')
                Mana -= 10
                auswahl = False
            elif ant == 3 and Mana <10:
                print('Du hast nicht genug Mana')
                continue        
            elif ant == 4 and Mana >= 6:
                    gefroren = Eis(Krit)
                    Mana -= 6
                    auswahl = False
            elif ant == 4 and Mana < 6:
                print('Du hast nicht genug Mana')
                continue                         
            elif ant == 5:
                HP = trankHeal(SpielerHP,SpielerMaxHP)
                SpielerHP = HP
                auswahl = False
                trank -= 1
            elif ant == 5 and trank <=0:
                print('Du hast keine Tränke mehr')    
                continue
                                

        if Schütze == 1:
            print('Das sind deine Optionen:')
            print('option 1: Angriff')
            print('option 2: Pfeilhagel Mana Kosten 5')
            print('option 3: Kritshot Mana Kosten 3')
            print('option 4: Salve Mana Kosten 3')
            print('option 5: Heiltrank Stück;',trank)
            ant = int(input('Du willst 1 , 2 ,3 , 4, 5 ?\n'))
            Krit = random.randint(0,2)
            if ant == 1:
                schadengegner,nextAtt = Schaden(DMG,Krit,GegnerRüstung,nextAtt)
                GegnerHP = GegnerHP - schadengegner
                print('Du hast den Feind',schadengegner,'Schaden verursacht, er hat nun noch',GegnerHP,'HP')
                auswahl = False
            elif ant == 2 and Mana >= 5:   
                schaden = pfeilhagel(DMG,GegnerRüstung)
                GegnerHP = GegnerHP - schaden
                print('Der Gegner erhält',schaden,'Schaden und sieht beinahe aus wie ein Mettigel')
                print('Er hat nun',GegnerHP,'Leben')
                Mana -= 5 
                auswahl = False
            elif ant == 2 and Mana < 5:
                print('Du hast nicht genug Mana')
                continue        
            elif  ant == 3 and Mana >= 3:
                schaden = KritShot (DMG,GegnerRüstung)
                KritShot (DMG,GegnerRüstung)                 
                GegnerHP = GegnerHP - schaden
                print('Der Gegner hat nun',GegnerHP,'Leben, der Gegner staunt nicht schlecht')
                Mana -= 3
                auswahl = False
            elif ant == 3 and Mana < 3:
                print('Du hast nicht genug Mana')
                continue       
                
            elif ant == 4 and Mana >= 3:
                schaden = salve(DMG,Krit,GegnerRüstung)
                GegnerHP = GegnerHP - schaden
                print('Der Gegner erleidet Schaden von',schaden,'und hast nun',GegnerHP,'Leben')   
                Mana -= 3 
                auswahl = False
            elif ant == 4 and Mana < 3:
                print('Du hast nicht genug Mana')
                continue        
            elif ant == 5:
                HP = trankHeal(SpielerHP,SpielerMaxHP)
                SpielerHP = HP
                auswahl = False
                trank -= 1
            elif ant == 5 and trank <=0:
                print('Du hast keine Tränke mehr')    
                continue
                                

        if Assasine == 1:
            print('Das sind deine Optionen:')
            print('option 1: Angriff')
            print('option 2: Unsichtbarkeit Mana Kosten 5')
            print('option 3: Gift Mana Kosten 3')
            print('option 4: Dolchwurf Mana Kosten 3')
            print('option 5: Heiltrank Stück;',trank)
            ant = int(input('Du willst 1 , 2 ,3 , 4, 5 ?\n'))
            Krit = random.randint(0,2)
            if ant == 1:
                schadengegner,nextAtt = Schaden(DMG,Krit,GegnerRüstung,nextAtt)
                dmg = GegnerHP - schadengegner
                GegnerHP = dmg
                print('Du hast den Feind',schadengegner,'Schaden verursacht, er hat nun noch',GegnerHP,'HP')
                auswahl = False
            elif ant == 2 and Mana >= 5:   
                Sneakschaden = unsichtbarkeit(DMG,Krit,GegnerRüstung)
                ausweichen = True
                nextAtt += 1
                print('Du wirst zum Schatten und der Gegner hat bis zu deinem nächsten Angriff probleme dich zu Treffen')
                Mana -= 5
                auswahl = False
            elif ant == 2 and Mana <5:
                print('Du hast nicht genug Mana')
                continue        
            elif  ant == 3 and Mana >= 3: 
                Giftschaden,Giftdauer = gift(DMG,Giftdauer) 
                print('Der Gegner ist nun 5 Runden vergiftet mit jeweils',Giftschaden,'Schaden')   
                Mana -= 3
                auswahl = False
            elif ant == 3 and Mana <3:
                print('Du hast nicht genug Mana')
                continue            
            elif ant == 4 and Mana >= 3:
                schaden, GegnerRüstung = dolchwurf(DMG,Krit,GegnerRüstung)
                GegnerHP = GegnerHP - schaden
                print('Der Gegner erleidet Schaden von',schaden,'und hast nun',GegnerHP,'Leben')  
                Mana -= 3  
                auswahl = False
            elif ant == 4 and Mana < 3:
                print('Du hast nicht genug Mana')
                continue    
            elif ant == 5:
                HP = trankHeal(SpielerHP,SpielerMaxHP)
                SpielerHP = HP
                auswahl = False
                trank -= 1
            elif ant == 5 and trank <=0:
                print('Du hast keine Tränke mehr')    
                continue
                                

                                
                        
            



    return Krieger,Magier,Schütze,Assasine,trank,Mana,MaxMana,DMG,SpielerHP,SpielerMaxHP,SpielerRüstung,GegnerHP,GegnerRüstung,GegnerDMG,Giftdauer,Giftschaden,blocken,schutz,gefroren,Sneakschaden,ausweichen,nextAtt,runde,win



#Krieger,Magier,Schütze,Assasine,trank,Mana,MaxMana,DMG,SpielerHP,SpielerMaxHP,SpielerRüstung,GegnerHP,GegnerRüstung,GegnerDMG,Giftdauer,Giftschaden,blocken,schutz,gefroren,Sneakschaden,ausweichen,nextAtt,runde 
# 1        2        3       4       5    6      7    8     9           10            11           12         13        14        15         16         17      18         19          20         21    22      23
#kampfrunde(0,0,0,1,2,6,6,10,70,70,5,200,10,20,        0,1,0,0,0,0,False,False,1)
#          1 2 3 4 5 6 7 8  9  10 11 12 13 14        15 16 17 18 19 20 21  22 23

schutz = 0
giftschaden = 0
spieler = None
krieger = 0
magier = 0
schütze = 0
assasine = 0
giftdauer = 0
blocken = 0
gefroren = 0
sneakschaden = 0
ausweichen = False
nextAtt = 0
runde = 1
win = False

print('Willkommen Abenteurer im Niemandland')
time.sleep(1)
name = input('Wie lautet dein Name?\n' ).title()
time.sleep(1)
print(f'{name},welche Klasse wärst du gerne?')
print('Zur Auswahl stehen dir diese Klassen:')
time.sleep(3)
print('Option 1:   Krieger')
print('HP : 100')
print('Stärke : 18 ')
print('Verteidigung : 8')
print('Mana : 2\n')
time.sleep(2)
print('Option 2:   Magier')
print('HP : 70')
print('Stärke : 11 ')
print('Verteidigung : 2')
print('Mana : 15\n')
time.sleep(2)
print('Option 3:   Schütze')
print('HP : 70')
print('Stärke : 14 ')
print('Verteidigung : 6')
print('Mana : 6\n')
time.sleep(2)
print('Option 4: Assasine')
print('HP : 70')
print('Stärke : 13 ')
print('Verteidigung : 5')
print('Mana : 6\n')
time.sleep(2)


bestaetigung = False


while bestaetigung == False:
    option = int(input('Welche Klasse soll es sein?\n 1 ,2 ,3 oder 4?\n'))
    if option == 1 :
        
        print('Du willst also Krieger sein?')
        janein = input('ja/nein\n').lower()
        if janein == 'ja':
            bestaetigung = True
            spieler = 'Krieger'
        elif janein == 'nein':
            continue
        else:
            continue
    if option == 2 :
        
        print('Du willst also Magier sein?')
        janein = input('ja/nein\n').lower()
        if janein == 'ja':
            bestaetigung = True
            spieler = 'Magier'
        elif janein == 'nein':
            continue
        else:
            continue
    if option == 3 :
        
        print('Du willst also Schütze sein?')
        janein = input('ja/nein\n').lower()
        if janein == 'ja':
            bestaetigung = True
            spieler = 'Schütze'
        elif janein == 'nein':
            continue
        else:
            continue
    if option == 4 :
        
        print('Du willst also Assasine sein?')
        janein = input('ja/nein\n').lower()
        if janein == 'ja':
            bestaetigung = True
            spieler = 'Assasine'
        elif janein == 'nein':
            continue
        else:
            continue
        
    
time.sleep(2)
bestaetigung = False
while bestaetigung == False:                
    reise = input(f'{spieler}, {name} bist du bereit für eine lange Reise?\nja/nein\n')
    if reise == 'nein':
        print('okay....')
        time.sleep(2)
        reise = input('Bist du Sicher?')
        if reise == 'nein':
            print('Super dann fangen wir mal an !')
            break
        elif reise == 'ja':
            time.sleep(2)
            print('Mach einen Abgang....')
            time.sleep(3)
            print('GAME OVER')
            time.sleep(5)
            sys.exit(0)
    elif reise == 'ja':
        print('Super dann fangen wir mal an !')
        break        
    else:
        print('Was soll mir das Sagen....?')
        time.sleep(2)
        continue    
print('Also gut, ich werde dir eine Startausrüstung geben')
goldbeutel = 10
time.sleep(2)
print( 'Spieler erhält: Goldbeutel(Inhalt,',goldbeutel,'Gold')
time.sleep(1)
print( 'Spieler erhält: Standardausrüstung')
time.sleep(1)
print('Spieler erhält 2 Heiltränke')
trank = 2

if spieler == 'Krieger':
    spielerHP = 100
    spielerMaxHP = 100
    spielerStr = 18
    spielerVer = 8
    maxmana = 2
    mana = 2
    krieger = 1
elif spieler == 'Magier':
    spielerHP = 70
    spielerMaxHP = 70
    spielerStr = 11
    spielerVer = 2
    maxmana = 15
    mana = 15
    magier = 1
    
elif spieler == 'Schütze':
    spielerHP = 70
    spielerMaxHP = 70
    spielerStr = 13
    spielerVer = 5
    maxmana = 6
    mana = 6
    schütze = 1
elif spieler == 'Assasine':
    spielerHP = 70
    spielerMaxHP = 70
    spielerStr = 14
    spielerVer = 2
    mana = 6
    maxmana = 6
    assasine = 1

maxspielervert = spielerVer
maxspielerstr = spielerStr


print('Deine Aufgabe ist es den Bösen Diktator Ilker zu besiegen')
time.sleep(1)
print('Dazu musst du in den Dungeon der "Demokratie"')
time.sleep(1)
print('Dort werden üble gestalten auf dich warten, zudem Rätsel und Fallen ')
time.sleep(1)
print('Ich wünsche dir viel Glück Abenteurer')
time.sleep(1)
print('')
print('')
print('')
print('Du machst dich auf dem weg zum Dungeon.\n Doch dort warten auf dem Weg Banditen, die dir den Weg abschneiden.\n Sie würden dich durchlassen, wenn du Ihnen dein komplettes Gold überlässt.')
ant = int(input('Du hast die Wahl\n Kämpfen = 1 Gold abgeben = 0\n'))
if ant == 0:
    goldbeutel = 0
    print('Dein Geldbeutel ist nun leer, doch Sie lassen dich Passieren.')
else:
    print('Du entscheidest dich zu kämpfen')
    print('Einer der Banditen lacht dich aus und fordert sich zum Zweikampf')
    gegnerHP = 80
    gegnerrüstung = 8
    gegnerdmg = 13
    (krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win) = kampfrunde(krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win)
    if win == False:
        sys.exit()
    spielerHP,mana = recover(spielerMaxHP,maxmana)
    print('Du hast gesiegt. Die Banditen halten sich an den Ehrenkodex des Zeitkampfs und lassen dich passieren')    
    spielerVer,spielerStr = resetVerAng(maxspielervert,maxspielerstr)

platz(2)
print('Auf deiner Reise findest du einen Bettler, er fragt dich nach einer Münze möchetest du Ihm eine geben?\n')
ant = int(input('1 = ja| 2 = nein\n'))
platz(1)
karma = 0
if ant == 1 and goldbeutel >= 1:
    print('Der Bettler freut sich und bedankt sich vielmals')
    print('Eventuell bringt dir das Gute Karma Später etwas')
    goldbeutel -= 1
    karma += 1
elif ant == 1 and goldbeutel <1:
    print('Du kannst den Bettler leider nichts geben, Du hast keine Münzen mehr')    
elif ant == 2:
    print('Du sagst den Bettler dass du nicht zu verteilen hättest')  
    karma -= 1
else:
    print('Du ignorierst den Bettler und gehst weiter')
    karma -= 1
platz(2)
print('Du reist weiter , zunächst über grüne Wiesen anschließend durch Gebirige')
platz(1)
print('Als du im Gebirge ankommst spührst die Kälte in deinem Nacken')
platz(1)
print('GRRRzz')
platz(1)
print('....')
platz(1)
print('Du wunderst dich was das für ein Geräusch war')
platz(2)
print('Plöztlich verspührst du schmerzen in deinem Rücken...')
platz(1)
print('Ein Kleiner Berggoblin hat dir in den Rücken geschlagen') 
platz(1)
spielerHP = spielerHP *0.5
print('Du hast nur noch die hälfte deines Lebens')
print('Doch es ist ein kleiner Goblin, Du könntest es Schaffen')
platz(1)
print('Es kommt zum Kampf')
gegnerHP = 55
gegnerrüstung = 8
gegnerdmg = 15
win = False
(krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win) = kampfrunde(krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win)
spielerVer,spielerStr =resetVerAng(maxspielervert,maxspielerstr)
if win == False:
    sys.exit()        
zufallsgold = random.randint(3,7)    
print('Du hast die Schlacht überstanden,du plünderst den Goblin')
goldbeutel = goldstand(goldbeutel)
platz(1)
print('Du findest eine Höhle in den Bergen, die dich vor dem Wind schützt')
print('Du entscheidest dort eine Rast zu machen und wieder zu Kräften zu kommen')
platz(2)
spielerHP,mana = recover(spielerMaxHP,maxmana)
print('In der Höhle siehst du eine merkwürdige Waffe..')
ant = int(input('Möchtest du sie aufheben?\n1 = ja | 2 = nein\n'))
if ant == 1:
    print('Du merkst wie du mehr Kraft erhälst jedoch saugt sie dir auch einiges an Lebenskraft aus')
    ant = int(input('Willst du die Waffe behalten und nutzen?\n1 = ja | 2 = nein\n'))
    if ant == 1:
        print('Du erhälst mehr Angriff aber weniger Maximalesleben')
        spielerStr =spielerStr * 1,2
        spielerMaxHP = spielerMaxHP * 0.8
        platz(1)
        print('Maxhp:',spielerMaxHP,'|Stärke:',spielerStr)
        maxspielerstr = spielerStr
        maxspielerstr = spielerVer

    else:
        print('Du lässt die Waffe liegen und machst dich weiter auf den Weg')    
elif ant == 2:
     print('Du lässt die Waffe liegen und machst dich weiter auf den Weg')    

platz(3)
print('Du erreichst endlich den Dungeon') 
platz(1)
print('Doch ein Torwächter steht vor der Tür')
platz(1)
print('Er lässt dich nur passieren wenn du sein Rätsel löst')
platz(1)
spielerHP, tor_offen = torwaechter_raetsel(spielerHP)

if tor_offen:
    print("Du betrittst den Dungeon der Demokratie...")
else:
    print("GAME OVER")


spieler_pos = (0, 0)  # Tulpel zum Speichern der Koordinaten ansich un veränderbar ohne entpackung

while True and spielerHP >= 0:
   
    gegnerHP = 50
    gegnerrüstung = 8
    gegnerdmg = 13
    

    
    karte_anzeigen(karte, besucht, spieler_pos)
    

    if karte[spieler_pos[1]][spieler_pos[0]] == "A":
        print("\n Du betritts den Eingang zur nächsten Etage!")
        break
    elif karte[spieler_pos[1]][spieler_pos[0]] == 'X' and besucht[spieler_pos[1]][spieler_pos[0]] == False:
        print('Du bist direkt in eine Falle gelaufen')
        prozent_schaden = spielerHP* 0.2
        spielerHP -= prozent_schaden
  
        print('Erhaltener Schaden:',prozent_schaden ,'SpielerHp:',spielerHP)
    elif  karte[spieler_pos[1]][spieler_pos[0]] == 'S' and besucht[spieler_pos[1]][spieler_pos[0]] == False:
        print('In einem kleinen Raum findest du etwas Gold')
        goldbeutel = goldstand(goldbeutel) 
      
    elif karte[spieler_pos[1]][spieler_pos[0]] == 'G' and besucht[spieler_pos[1]][spieler_pos[0]] == False:
            print('Du triffts auf einen kleinen bösen Gnom')
            (krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win) = kampfrunde(krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win)
            spielerVer,spielerStr = resetVerAng(maxspielervert,maxspielerstr)
            
            goldbeutel = goldstand(goldbeutel) 
            karte_anzeigen(karte, besucht, spieler_pos)

    raum_betreten(spieler_pos, besucht)   

    print('  >>Legende<<')
    print('')
    print('P = Player')
    print('x = Falle')
    print('? = Unentdeckt')
    print('S = Schatz')
    print('G = Gegner')
    print('A = Ausgang')
    print('E = Eingang')
    print('. = Leer')
    print('')


    print("\nBewegen mit:")
    print("W = hoch | S = runter | A = links | D = rechts")
    richtung = input("Dein Zug: ").lower()

    spieler_pos = bewege_spieler(spieler_pos, richtung, karte)

if spielerHP <= 0:
    print('GAME OVER')
    sys.exit(0)
else:
    print('Am Anfang der nächsten Etage warten ein Händler sammt Gesellschaft')
    print('Du versuchst mit Ihm zu Handeln')     

goldbeutel, spielerHP, spielerMaxHP, spielerStr, spielerVer, mana, maxmana, trank = haendler_upgrade(
    goldbeutel, spielerHP, spielerMaxHP, spielerStr, spielerVer, mana, maxmana, trank
)
maxspielerstr = spielerStr
maxspielerstr = spielerVer
spielerVer,spielerStr = resetVerAng(maxspielervert,maxspielerstr)

spieler_pos = (0, 0)  # Tulpel zum Speichern der Koordinaten ansich un veränderbar ohne entpackung

while True and spielerHP >= 0:
   
    gegnerHP = 80
    gegnerrüstung = 5
    gegnerdmg = 15
    

    
    karte_anzeigen(karte2, besucht2, spieler_pos)
    

    if karte2[spieler_pos[1]][spieler_pos[0]] == "B":
        print("\n Du triffst auf eine bedrohliche Aura die dir durch Mark und Bein gehst!")
        time.sleep(1)
        print('Sie scheint aus dem Raum zu kommen den du grade entgegen gehst')
        time.sleep(1)
        print('....')
        break
    elif karte2[spieler_pos[1]][spieler_pos[0]] == 'X' and besucht2[spieler_pos[1]][spieler_pos[0]] == False:
        print('Du bist direkt in eine Falle gelaufen')
        prozent_schaden = spielerHP* 0.2
        spielerHP -= prozent_schaden
  
        print('Erhaltener Schaden:',prozent_schaden ,'SpielerHp:',spielerHP)
    elif  karte2[spieler_pos[1]][spieler_pos[0]] == 'S' and besucht2[spieler_pos[1]][spieler_pos[0]] == False:
        print('In einem kleinen Raum findest du etwas Gold')
        goldbeutel = goldstand(goldbeutel) 
      
    elif karte2[spieler_pos[1]][spieler_pos[0]] == 'G' and besucht2[spieler_pos[1]][spieler_pos[0]] == False:
            print('Du triffts auf einen kleinen bösen Gnom')
            (krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win) = kampfrunde(krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win)
            spielerVer,spielerStr = resetVerAng(maxspielervert,maxspielerstr)
            
            goldbeutel = goldstand(goldbeutel) 
            karte_anzeigen(karte, besucht, spieler_pos)
    elif karte2[spieler_pos[1]][spieler_pos[0]] == 'H':
            print('Du stattest den Händler einen Besuch ab')
            goldbeutel, spielerHP, spielerMaxHP, spielerStr, spielerVer, mana, maxmana, trank = haendler_upgrade(
            goldbeutel, spielerHP, spielerMaxHP, spielerStr, spielerVer, mana, maxmana, trank
            )
            maxspielerstr = spielerStr
            maxspielerstr = spielerVer
            spielerVer,spielerStr = resetVerAng(maxspielervert,maxspielerstr)        

    raum_betreten(spieler_pos, besucht)   

    print('  >>Legende<<')
    print('')
    print('P = Player')
    print('x = Falle')
    print('? = Unentdeckt')
    print('S = Schatz')
    print('G = Gegner')
    print('H = Händler (mehrfach besuchbar)')
    print('B = Boss')
    print('E = Eingang')
    print('. = Leer')
    print('')


    print("\nBewegen mit:")
    print("W = hoch | S = runter | A = links | D = rechts")
    richtung = input("Dein Zug: ").lower()

    spieler_pos = bewege_spieler(spieler_pos, richtung, karte)

if spielerHP <= 0:
    print('GAME OVER')
    sys.exit(0)

else:
    print('Du vorderst den Diktator zum Duell heraus')
    time.sleep(1)
    print('Zeit für ein ..D\n ..D\n ..D\n DUEL')     


gegnerHP = 250
gegnerdmg = 30
gegnerrüstung = 10


(krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win) = kampfrunde(krieger,magier,schütze,assasine,trank,mana,maxmana,spielerStr,spielerHP,spielerMaxHP,spielerVer,gegnerHP,gegnerrüstung,gegnerdmg,giftdauer,giftschaden,blocken,schutz,gefroren,sneakschaden,ausweichen,nextAtt,runde,win)
spielerVer,spielerStr = resetVerAng(maxspielervert,maxspielerstr)



if spielerHP <= 0:
    print('GAME OVER')
    sys.exit(0)

else:
    print('Du gewinnst die Schlacht')
    platz(1)
    print('Du hörst den besiegten Diktator Ilker, seine letzten Worte sagen..\n')
    platz(1)
    print('Im..')     
    platz(1)
    print('Schach..')
    platz(1)
    print('hätte..')      
    platz(1)
    print('Ich..')
    platz(1)
    print('triumphiert..')  
    platz(5)
    print('THE END')            
    

