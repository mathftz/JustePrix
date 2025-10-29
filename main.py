import random

# Générer un nombre aléatoire entre 1 et 10000
nombre_a_trouver = random.randint(1, 10001)

trouve = False
nb_tentatives = 0

while not trouve:
    # Demander à l'utilisateur de deviner le nombre
    nombre_saisis = int(input("Devinez le nombre entre 1 et 10000 : "))

    # Incrémenter le nombre de tentatives de 1
    nb_tentatives = nb_tentatives + 1

    if nombre_saisis > nombre_a_trouver:
        print("Le nombre saisi est trop grand")

    elif nombre_saisis == nombre_a_trouver:
        print(f"Gagné en {nb_tentatives} tentatives")
        trouve = True

    else:
        print("Le nombre saisi est trop petit")

print("Fin du jeu")
