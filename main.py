import random


def demander_nombre_magique(nb_min, nb_max):
    nb_donner_int = 0
    while nb_donner_int == 0:
        nb_donner_str = input(f"Proposez un nombre entre {nb_min} et {nb_max} : ")
        try:
            nb_donner_int = int(nb_donner_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez. ")
        else:
            if nb_donner_int < nb_min or nb_donner_int > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                nb_donner_int = 0
    return nb_donner_int


def demander_nombre(nombre_type):
    nb_donner_int = 0
    while nb_donner_int == 0:
        nb_donner_str = input(f"Choisissez {nombre_type} : ")
        try:
            nb_donner_int = int(nb_donner_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez. ")
    return nb_donner_int


nombreMagiqueMin = demander_nombre("la valeure minimum du nombre magique")
nombreMagiqueMax = demander_nombre("la valeure maximum du nombre magique")
nombreDeVies = demander_nombre("votre nombre de vies")
NOMBRE_MAGIQUE = random.randint(nombreMagiqueMin, nombreMagiqueMax)

nombreJoueur = 0
"""
===========================================BOUCLE FOR=====================================================
"""

gagne = False
for i in range(0, nombreDeVies):
    vies = nombreDeVies-i
    print(f"Il vous reste {vies} vie !")
    nombreJoueur = demander_nombre_magique(int(nombreMagiqueMin), int(nombreMagiqueMax))
    if nombreJoueur == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagner !")
        gagne = True
        break
    elif nombreJoueur > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit.")
    else:
        print("Le nombre magique est plus grand.")


if not gagne:
    print(f"Vous avez perdu. Le nombre magique etait {NOMBRE_MAGIQUE}")

"""
=======================================BOUCLE WHILE===================================================
"""

"""
nombreJoueur = 0
vies = nombreDeVies
while not nombreJoueur == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vie !")
    nombreJoueur = demander_nombre_magique(int(nombreMagiqueMin), int(nombreMagiqueMax))
    if nombreJoueur == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagner !")
    elif nombreJoueur > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit.")
        vies -= 1
    else:
        print("Le nombre magique est plus grand.")
        vies -= 1


if vies == 0:
    print(f"Vous avez perdu. Le nombre magique etait {NOMBRE_MAGIQUE}")

"""
input()
