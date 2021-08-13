# MARTIN Tanguy
# Projet APL Sudoku
# fichier case.py

import random # Pour les fonctios nécessitant de l'aléatoire.


def CreerCase(x,y): # Créer un dictionnaire pour simuler une structure de case. (Créer une case de coordonnées x, y).
    c={} # Déclaration / Initialisation
    c["vérouillée"]=False #  Indique si la case peut être modifiée ou non.
    c["possibilités"]=[True,True,True,True,True,True,True,True,True,True]  # Tableau de Booléens décrivant la possibilité d'avoir ou non un chiffre dans la case. Sert à la génération est à la vérification.
    c["ch"]=0 # Le chiffre contenu dans la case.
    c["x"]=x # La coordonnée x (la ligne de la case).
    c["y"]=y # La coordonnée y (la colonne de la case).

    return c

def PlacerDansCase(c,ch): # Place le chiffre passe en entrée dans la case.
    if c["vérouillée"] :
        print("Case Préremplie, impossible de la modifier !")

    c["ch"]=ch

    return None

def EnleverDeCase(c,val): # Met la possibilité d'avoir val dans la case à Faux (False)
    c["possibilités"][val]=False
    return None

def CoordCaseX(c): # Retourne la coordonnée x (la ligne de la case)
    return c["x"]

def CoordCaseY(c): # Retourne la coordonnée y (la colonne de la case)
    return c["y"]

def ValeurCase(c): # Retourne la valeur de la case (par défaut elle vaut 0 car vide)
    return c["ch"]

def PossibleCase(c,val): # Renvoie Vrai (True si il est possible d'avoir la valeur dans la case.)
    return c["possibilités"][val]

def NbPossibiliteCase(c): # Renvoie le nombre de possibilités que possède une case. (Le nombre de Vrai (True) que contient son tableau "possibilités").
    n=0
    i=1

    while i <= 9 :
        if PossibleCase(c,i) :
            n+=1
        
        i+=1
    
    return n

def ListePossibleCase(c) : # Liste les chiffres pouvant être mis dans la case (ex: si dans la ligne de la case il y un 1 et de la colonne de la case il y a un 3 alors la liste sera [2,4,5,...,9]).
    i=1 # Varaible compteur
    lp=[] # Sortie liste d'entiers

    while i <= 9 :
        if PossibleCase(c,i) : # Si il est possible d'avoir le chiffre i dans la case alors on l'ajoute dans la liste.
            lp.append(i)
        
        i+=1
    
    return lp

def EstVideCase(c): # Renvoie Vrai (True) si la case est vide (valeur = 0).
    if c["ch"]==0 :
        return True
    
    return False

def EstVerouilleeCase(c): # Renvoie Vrai (True) si la case est vérouillée (préremplie)
    return c["vérouillée"]

def AleaPossibleCase(c): # Tir au sort une valeur possible d'être mise dans la case.
    deb=c["possibilités"].index(True)# Récupère le premier indice pour lequel la valeur est Vrai (True).

    while True: # Tan que l'on ne trouve pas un indice pour lequel il est possible de placer le chiffre dans la case, on continue.
        n=random.randint(deb,9) # Sélectionner un indice entre l'indice deb (choisi plus haut) et l'indice max (9).
        
        if PossibleCase(c,n): # Si la valeur de la possibilité à la position de l'indice est Vrai (True). 
            return n

def ResetCases(c): # Remet les cases à vide (à 0), et remet toutes les possibilités à Vrai (True).
    i=0
    while i<10:
        c["possibilités"][i]=True
        i+=1
    c["ch"]=0
    c["vérouillée"]=False
    
    return None