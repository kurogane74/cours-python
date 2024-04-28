def main():
    nombre_a_gauche = input("entré un nombre entier:")
    nombre_a_droite = input("entré un nombre entier: ")
    operation = input("entré un symbole d'operation (+,-,*,/) :")
    resultat = 0
    
    if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
        print("Erreur: les deux nombres doivent être des nombres entiers")
    else:
        nombre_a_gauche = int(nombre_a_gauche)
        nombre_a_droite = int(nombre_a_droite)
    
        match operation:
            case "+":
                resultat = nombre_a_gauche + nombre_a_droite
            case "-":
                resultat = nombre_a_gauche - nombre_a_droite
            case "*":
                resultat = nombre_a_gauche * nombre_a_droite
            case "/":
                if nombre_a_droite == 0:
                    print("Erreur: impossible de diviser par zéro.")
                else:
                    resultat = nombre_a_gauche / nombre_a_droite
            case _:
                print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
        
        print(f"Le résultat de l'opération est: {resultat}")
            
    
    
    
    


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()