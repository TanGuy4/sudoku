# MARTIN Tanguy
# Projet APL Sudoku
# fichier grille.py

import case # On importe les fonctions du fichier case.py
import random

# Grille par défaut avant que l'on ajoute la structures des cases (dictionnaires dedans).
grille=[[[],[],[],  [],[],[],   [],[],[]],
        [[],[],[],  [],[],[],   [],[],[]],
        [[],[],[],  [],[],[],   [],[],[]],

        [[],[],[],  [],[],[],   [],[],[]],
        [[],[],[],  [],[],[],   [],[],[]],
        [[],[],[],  [],[],[],   [],[],[]],

        [[],[],[],  [],[],[],   [],[],[]],
        [[],[],[],  [],[],[],   [],[],[]],
        [[],[],[],  [],[],[],   [],[],[]]]

# Constantes pour les types de zone
ligne="ligne"
colonne="colonne"
carre="carre" # (sous-grille)

def CreerGrille(): # Créer / Initialise la grille en insérant la structure des cases (dictionnaire) (cf fichier case.py).
    x=0

    while x < 9 :
        y=0

        while y < 9 :
            grille[x][y]=case.CreerCase(x,y)
            y+=1
        
        x+=1
    
    return grille

def IndiceCarre(x,y): # Permet de calculer l'indice d'un carre (d'une sous-grille)
    if x<3 and y<3:
        return 0
    if x<3 and (y>=3 and y<6):
        return 1
    if x<3 and y>=6:
        return 2
    if (x>=3 and x<6) and y<3:
        return 3
    if (x>=3 and x<6) and (y>=3 and y<6):
        return 4
    if (x>=3 and x<6) and y>=6:
        return 5
    if x>=6 and y<3:
        return 6
    if x>=6 and (y>=3 and y<6):
        return 7
    if x>=6 and y>=6:
        return 8

def CaseDansGrille(g,x,y): # Renvoie la case de la grille se trouvant à la postion x, y.
    return g[x][y]

def CaseVideDansGrille(g): # Renvoie une case vide (dont la valeur est 0) de la grille sélectionner aléatoirement.
    if NbCasesRempliesDansGrille==81:
        return None
    
    x=random.randint(0,8)
    y=random.randint(0,8)

    essai=0
    while not case.EstVideCase(CaseDansGrille(g,x,y)) and essai < 200: # Si le premier renvoie une case remplie alors on recommence avec une limite de 200 essais pour éviter une boucle "infinie".
        x=random.randint(0,8)
        y=random.randint(0,8)
        essai+=1
    
    return CaseDansGrille(g,x,y)

def RemplirGrille(g): # Rempli 36 cases de la grille aléatoirement, en fonctionne des possibilités des cases.
    i=0
    while i < 36:
        c=CaseVideDansGrille(g)
        n=0
        while n==0:
            n=case.AleaPossibleCase(c) # voir fichier case.py
        PlacerDansGrille(g,n,case.CoordCaseX(c),case.CoordCaseY(c))
        c["vérouillée"]=True
        i+=1

    return None

def AfficherGrille(g): # Procédure affichant la grille.
    x=0
    l=['A','B','C','D','E','F','G','H','I'] # Lettre des lignes.

    print("    1 2 3  4 5 6  7 8 9") # Affiche le numero des colonnes

    while x <= 9 :
        if x%3==0 : # défini si la ligne de sépartion doit être simple ou double (simple si sépare des cases d'une même sous-grille (carré), double si sépare des carrés (sous-grilles)).
            j=2
        else:
            j=1
        
        k=0

        while k < j : # Boucle permettant l'affichage de la ligne de séparation (simple ou double)
            i=0

            print("  ",end="")
            while i <= 18 :
                if i%6==0 :
                    print("++",end="")
                else:
                    print("-",end="")
                
                i+=1
            
            print()
            k+=1
        
        if x==9:
            return None
        
        y=0

        print(l[x],end=" ") # Affiche la lettre de la ligne.

        while y < 9 : # Boucles pour afficher les cases
            if y%3==0 : # Définie l'paisseur du trait de séparation (comme pour la ligne de séparation).
                print("|",end="")
            
            print("|",end="")
            c=CaseDansGrille(g,x,y)

            if case.EstVideCase(c) : # Si la case est vide (valeur = 0) on affiche un "blanc", un espace.
                print(" ",end="")
            else:
                print(case.ValeurCase(c),end="") # le end="" évite le retour à la ligne automatique de Python.
            
            y+=1
        print("||")
        x+=1
    
    return None

def ParcourirZoneGrille(g,z,indice): # Fonction parcourant une zone donnée de la grille (ligne, colonne ou carre) d'indice donné.
    if z==ligne: # Pour les lignes
        for y in range(0,9):
            yield CaseDansGrille(g,indice,y) # La fonction yield marche qu'avec les boucle for (je suis pas surs). Elle permet de renvoyer une à une les case.
    
    if z==colonne: # Pour les colonnes
        for x in range(0,9):
            yield CaseDansGrille(g,x,indice) # Idem
    
    if z==carre: # Pour les sous-grilles
        if indice<3: # On cherche la ligne d'origine de la sous-grille à partir de l'indice.
            ox=0
        elif (indice>=3 and indice<6):
            ox=3
        elif indice>=6:
            ox=6
        
        if indice in [0,3,6]: # A partir de l'indice on détermine la colonne d'origine de la sous-grille.
            oy=0
        elif indice in [1,4,7]:
            oy=3
        elif indice in [2,5,8]:
            oy=6
        
        for x in range(0,3):
            for y in range(0,3):
                yield CaseDansGrille(g,ox+x,oy+y) # Idem que pour les lignes et les colonnes.

def ParcourirGrille(g): # Parcours les cases de la grille et les renvoie une par une.
    for x in range(0,9):
        for y in range(0,9):
            yield CaseDansGrille(g,x,y) # Idem que dans la fonction ParcourirZoneGrille
        

def PlacerDansGrille(g,val,x,y): # Place la valeur donnée dans la case de coordonnée x, y.
    case.PlacerDansCase(CaseDansGrille(g,x,y),val)
    
    if val==0: # Si on vide la case (utilisateur rentre 0), on ne recalcul pas les possibilités de la ligne, de la colonne et de la sous-grille dans lesquels se trouve la case remplie.
        return None

    for c in ParcourirZoneGrille(g,ligne,x): # Enlève la possibilité des autres cases de la ligne d'avoir la valeur val.
        case.EnleverDeCase(c,val)
    
    for c in ParcourirZoneGrille(g,colonne,y): # Enlève la possibilité des autres cases de la colonne d'avoir la valeur val.
        case.EnleverDeCase(c,val)
    
    for c in ParcourirZoneGrille(g,carre,IndiceCarre(x,y)): # Enlève la possibilité des autres cases de la sous-grille d'avoir la valeur val.
        case.EnleverDeCase(c,val)
    
    return None

def NbCasesRempliesDansGrille(g): # Renvoie le nombre de cases remplies dans la grille.
    n=0

    for c in ParcourirGrille(g):
        if not case.EstVideCase(c):
            n+=1
        
    return n

def NbCasesVidesDansGrille(g): # Renvoie le nombre de cases vides dans la grille.
    n=81-NbCasesRempliesDansGrille(g)

    return n

def NbPossibiliteZone(g,val,z,indice): # Renvoie le nombre de cases ayant une possibilité à Vrai (True) pour une valeur donnée.
    n=0

    for c in ParcourirZoneGrille(g,z,indice):
        if case.PossibleCase(c,val):
            n+=1
    
    return n

def DansZone(g,val,z,indice): # Renvoie Vrai (True) si la valeur donnée est dans la zone (ligne, colonne ou sous-grille) d'indice donné.
    for c in ParcourirZoneGrille(g,z,indice):
        if case.ValeurCase(c)==val:
            return True
    
    return False

def NbDansZone(g,val,z,indice): # Renvoie le nombre de fois qu'apparaît un élément donné dans une zone donnée.
    n=0

    for c in ParcourirZoneGrille(g,z,indice):
        if case.ValeurCase(c)==val:
            n+=1
        
    return n

def VerifGrille(g): # Vérifie si la grille peut être résolue ou non (Actuellement les grilles générer ne le sont pas)
    for c in ParcourirGrille(g):
        if case.EstVideCase(c) and case.NbPossibiliteCase(c)==0:
            return False
    
    i=0

    while i < 9 :
        j=1

        while j <= 9 : # Si un chiffre pas dans un zone n'a pas de possibilité, ou si il est présent plus d'une fois d'une zone alors, la grille est impossible à résoudre.
            if (not DansZone(g,j,ligne,i) and NbPossibiliteZone(g,j,ligne,i)==0) or (not DansZone(g,j,colonne,i) and NbPossibiliteZone(g,j,colonne,i)==0) or (not DansZone(g,j,carre,i) and NbPossibiliteZone(g,j,carre,i)==0) or NbDansZone(g,j,ligne,i)>1 or NbDansZone(g,j,colonne,i)>1 or NbDansZone(g,j,carre,i)>1:
                return False
            
            j+=1
        
        i+=1
    
    return True

def ResetGrille(g): # Remet la grille à vide
    for c in ParcourirGrille(g):
        case.ResetCases(c)
    
    return None
