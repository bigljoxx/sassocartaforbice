import random

# Simula una partita di sasso, carta e forbice
def gioco():
    opzioni = ["sasso", "carta", "forbice"]
    scelta_utente = input("Scegli sasso, carta o forbice: ").lower()

    if scelta_utente not in opzioni:
        print("Scelta non valida, riprova.")
        return

    scelta_computer = random.choice(opzioni)
    print(f"Il computer ha scelto: {scelta_computer}")

    if scelta_utente == scelta_computer:
        print("Pareggio!")
    elif (scelta_utente == "sasso" and scelta_computer == "forbice") or \
         (scelta_utente == "carta" and scelta_computer == "sasso") or \
         (scelta_utente == "forbice" and scelta_computer == "carta"):
        print("Hai vinto!")
    else:
        print("Hai perso!")