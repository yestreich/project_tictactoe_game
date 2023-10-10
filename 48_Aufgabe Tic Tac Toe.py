'''
#===============#

#== TicTacToe ==#

#===============#

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
    
    player1()                           
    

def player1():
    
    print(p1 + ", was möchtest du tun?")
    
    dec = -1                            
    while dec < 1 or dec > 2:
        #try:
            print("Spielfeld anzeigen: 1, Stein legen: 2")
            dec = int(input())
            if dec == 1:
                spielfeld()
                dec = -1                
            if dec == 2:
                steinlegen("x")
                
    if ergebnis() != True:              
        player2()


def player2():
    
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
                steinlegen("o")                   
    
    if ergebnis() != True:        
        player1()

def steinlegen(s):
    num = -1                                
    while num < 0:                          
        print()
        print("Du bist " + s + ". Auf welches Feld möchtest du dein Stein legen?")
        print()
        feld = str(input())
        if feld_list[feld] == feld:         
            feld_list[feld] = s
            spielfeld()                     
            ergebnis()                      
            num = 0                        
        else:
            #spielfeld()
            print("Dieses Feld ist belegt. Wähle ein anderes.")
            continue                        
            

def ergebnis():                             
    
    row1 = [feld_list["1"], feld_list["2"], feld_list["3"]] 
    row2 = [feld_list["4"], feld_list["5"], feld_list["6"]]
    row3 = [feld_list["7"], feld_list["8"], feld_list["9"]]

    col1 = [feld_list["1"], feld_list["4"], feld_list["7"]]
    col2 = [feld_list["2"], feld_list["5"], feld_list["8"]]
    col3 = [feld_list["3"], feld_list["6"], feld_list["9"]]

    dia1 = [feld_list["1"], feld_list["5"], feld_list["9"]]
    dia2 = [feld_list["3"], feld_list["5"], feld_list["7"]]
    
    check = [row1, row2, row3, col1, col2, col3, dia1, dia2]
    
    for i in check:                                 
        if i.count("x") == 3:                   
            print(p1 + " hat gewonnen.")
            return True
            
        elif i.count("o") == -3:                
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


