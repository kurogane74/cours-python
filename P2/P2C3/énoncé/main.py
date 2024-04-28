# Ecrivez vos fonctions ici
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4
def salaire_horaire(salaire_hebdomadaire, heure_travaille):
    return salaire_hebdomadaire / heure_travaille
def main():
    salaire_annuel = float(input("quel est votre salaire annuel "))
    heure_travaille = float(input("nombre d'heure travaille par semaine: "))
    mensuel = salaire_mensuel(salaire_annuel)
    hebdomadaire = salaire_hebdomadaire(mensuel)
    heure = salaire_horaire(hebdomadaire, heure_travaille)
    print("votre salaire horaire est de " , heure)
# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()