'''
#===============#

#== TicTacToe ==#

#===============#


TODO 

Finales Ergbnis wird 2mal gedruckt
'''

#Zellen-Nummerierung
feld_list = {"1" : "1", 
             "2" : "2", 
             "3" : "3", 
             "4" : "4", 
             "5" : "5", 
             "6" : "6", 
             "7" : "7", 
             "8" : "8", 
             "9" : "9"}

#Spielfeld mit ständigem Zugriff auf Zellennummerierung
def spielfeld():
    print()
    print("#"*13)
    print("# " + "  #" + "   #" + "   #")
    print("# " + feld_list["1"] + " # " + feld_list["2"] + " # " + feld_list["3"] + " #")
    print("# " + "  #" + "   #" + "   #")
    print("#"*13)
    print("# " + "  #" + "   #" + "   #")
    print("# " + feld_list["4"] + " # " + feld_list["5"] + " # " + feld_list["6"] + " #")
    print("# " + "  #" + "   #" + "   #")
    print("#"*13)
    print("# " + "  #" + "   #" + "   #")
    print("# " + feld_list["7"] + " # " + feld_list["8"] + " # " + feld_list["9"] + " #")
    print("# " + "  #" + "   #" + "   #")
    print("#"*13)
    print()
          
#Start
def starten():
    print("Name Spieler 1: ")
    global p1
    p1 = str(input())
    print("Name Spieler 2: ")
    global p2
    p2 = str(input())

    
    print("")
    print(p1 + ", starte das Spiel!")   #Bisher startet Spieler 1 jedes Spiel
    print()
    # global count                      #klappt irgendwie nicht. Ende wurde anders gelöst-
    # count = 0
    
    player1()                           
    

def player1():
    
    # if count > 9:
    #     ergebnis()
    # else:
    #     count += 1
    
    print(p1 + ", was möchtest du tun?")
    
    dec = -1                            #damit while-loop öfters laufen kann.
    while dec < 1 or dec > 2:
        #try:
            print("Spielfeld anzeigen: 1, Stein legen: 2")
            dec = int(input())
            if dec == 1:
                spielfeld()
                dec = -1                #damit while-loop aufrechterhalten bleibt. Nach dem steinlegen kommt direkt der nächste Spieler
            if dec == 2:
                steinlegen("x")
                
    if ergebnis() != True:              #Solang kein Gewinner feststeht, darf der nächste Spieler wieder spielen.
        player2()


def player2():
    
    # if count > 9:
    #     ergebnis()
    # else:
    #     count += 1
    
    print(p2 + ", was möchtest du tun?")
    
    dec = -1
    while dec < 1 or dec > 2:
        #try:
            print("Spielfeld anzeigen: 1, Stein legen: 2")
            dec = int(input())
            if dec == 1:
                spielfeld()
                dec = -1
            if dec == 2:
                steinlegen("o")             #Parameter um Zelle neu zu besetzen      
    
    if ergebnis() != True:        
        player1()

def steinlegen(s):
    num = -1                                #While-loop soll wegen möglicher Falscheingabe wiederholt werden können.
    while num < 0:                          
        print()
        print("Du bist " + s + ". Auf welches Feld möchtest du dein Stein legen?")
        print()
        feld = str(input())
        if feld_list[feld] == feld:         #Wenn die gewünschte Zelle in Dict drin ist, wird sie durch Parameter s ersetzt
            feld_list[feld] = s
            spielfeld()                     #Neues Spielfeld wird angezeigt
            ergebnis()                      #Nach jedem Zug muss in Funktion berechnet werden ob ein Gewinner feststeht
            num = 0                         #loop auflösen, da Stein gesetzt wurde
        else:
            #spielfeld()
            print("Dieses Feld ist belegt. Wähle ein anderes.")
            continue                        #Falls ein belegtes Feld ausgewählt wird, wird man neu aufgefordert.
            

def ergebnis():                             #Hier wird das Ergebnis nach jedem Stein neu berechnet
    
    row1 = [feld_list["1"], feld_list["2"], feld_list["3"]] #Listen mit den Reihen-,Spalten-, und Diagonalen-Elementen
    row2 = [feld_list["4"], feld_list["5"], feld_list["6"]]
    row3 = [feld_list["7"], feld_list["8"], feld_list["9"]]

    col1 = [feld_list["1"], feld_list["4"], feld_list["7"]]
    col2 = [feld_list["2"], feld_list["5"], feld_list["8"]]
    col3 = [feld_list["3"], feld_list["6"], feld_list["9"]]

    dia1 = [feld_list["1"], feld_list["5"], feld_list["9"]]
    dia2 = [feld_list["3"], feld_list["5"], feld_list["7"]]
    
    check = [row1, row2, row3, col1, col2, col3, dia1, dia2]
    
    for i in check:                                 
        if i.count("x") == 3:                   #Wenn in einem der Reihen, Spalten oder Diagonalen drei X-e sind: Gewonnen.
            print(p1 + " hat gewonnen.")
            return True
            
        elif i.count("o") == -3:                #Wenn in einem der Reihen, Spalten oder Diagonalen drei O-s sind: Gewonnen.
            print(p2 + " hat gewonnen.")
            return True

# def neuerunde():
#     print("Noch eine Runde? y, n")
#     if input().lower() == "y":
#         starten()
#     if input().lower() == "n":
#         print("Tschüss!")
#         quit()
  
    #%%
starten()


