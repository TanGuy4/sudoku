# MARTIN Tanguy
# Projet APL 1 Sudoku
# fichier sudoku.py

import grille # On importe les fonctions du fichier grille.py

g=grille.CreerGrille()

#grille.AfficherGrille(g)

'''for line in g:
    for case in line:
        for param in line:
            print(param)'''

grille.RemplirGrille(g)
j=0
while not grille.VerifGrille(g) and j < 200: # Si la grile n'est resolvable alors on la regenère avec un nombre d'essai limités à 200 pour éviter une boucle "infinie".
    grille.ResetGrille(g)
    grille.RemplirGrille(g)
    j+=1

#grille.AfficherGrille(g)

#print(j)
#print(grille.VerifGrille(g))

'''for line in g:
    for case in line:
        for param in line:
            print(param)''' # Me permetait de vérifier la structure des cases, de voir si elle était bien mises à jour.

'''grille.ResetGrille(g)

grille.AfficherGrille(g)

for line in g:
    for case in line:
        for param in line:
            print(param)'''

#print(grille.NbCasesRempliesDansGrille(g))
print(grille.VerifGrille(g))

def Completer(): # Demande à l'utilisateur la ligne puis la colonne de la case qu'il shouaite compléter et avec quelle valeur il veut la compléter.
    x=input("Enrez la lettre de ligne que vous shouaitez compléter (A-I) : ")
    x=x.upper()
    while x not in ['A','B','C','D','E','F','G','H','I']:
        print("Saisie Invaide !")
        x=input("Enrez la lettre de ligne que vous shouaitez compléter (A-I) : ")
        x=x.upper()
    
    x=ord(x)-64
    
    y=int(input("Entrez le numero de la colonne à compléter (1-9) : "))
    while y<1 or y>9:
        print("Saisie Invalide !")
        y=int(input("Entrez le numero de la colonne à compléter (1-9) : "))
    
    ch=int(input("Entrez le chiffre à mettre dans la case (1-9) : "))
    while ch<0 or ch>9:
        print("Saisie Invalide !")
        ch=int(input("Entrez le chiffre à mettre dans la case (1-9) (0 pour case vide): "))
    
    grille.PlacerDansGrille(g,ch,x-1,y-1)
    return None

def Menu():
    grille.AfficherGrille(g)
    print("""
    1 - Compléter la grille
    2 - Quitter
    
    Votre choix : """)
    choix=int(input())

    while choix not in [1,2]:
        print("Veuillez entrer un choix valide !")
        choix=int(input("Votre choix : "))
    
    if choix==1: # Choix 1 on complète la grille
        Completer()
    else: # Si non on quitte
        print("Au revoir et à bientôt !")
        exit(0)
    
    return None

while True: # Permet de revenir au menu après chaque étape (complémentation)
    Menu()
