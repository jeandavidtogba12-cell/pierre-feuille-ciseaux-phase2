import random

# Variable pour savoir si le jeu est actif
jeu_actif = False

# Fonction pour démarrer le jeu
def lancer_jeu():
    global jeu_actif
    jeu_actif = True
    lbl_resultat["text"] = "Choisis : Pierre, Feuille ou Ciseaux"

# Fonction pour déterminer le gagnant
def determiner_gagnant(joueur, ordi):
    if joueur == ordi:
        return "Égalité "
    elif (joueur == "Pierre" and ordi == "Ciseaux") or \
         (joueur == "Feuille" and ordi == "Pierre") or \
         (joueur == "Ciseaux" and ordi == "Feuille"):
        return "Tu as gagné "
    else:
        return "Tu as perdu "

# Fonction quand le joueur clique
def choix_joueur(choice):
    if not jeu_actif:
        lbl_resultat["text"] = "Clique sur 'Jouer' d'abord !"
        return
    
    choix_ordi = random.choice(["Pierre", "Feuille", "Ciseaux"])
    resultat = determiner_gagnant(choice, choix_ordi)

    lbl_resultat["text"] = (
        f"Ton choix : {choice}\n"
        f"Ordinateur : {choix_ordi}\n\n"
        f"{resultat}"
    )

# Fonction pour réinitialiser
def reinitialiser():
    global jeu_actif
    jeu_actif = False
    lbl_resultat["text"] = "Clique sur 'Jouer' pour commencer"

# Fonction pour quitter
def quitter():
    window.destroy()