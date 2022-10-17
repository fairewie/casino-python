from random import randrange
# nb_ordi =  randrange (1, 11, 1)
# if is_valid(nb_ordi, 1, 10) :
    
# print('Mon choix est = ', nb_ordi)

def is_valid(nb, floor, ceiling):
    return isinstance(nb, int) and floor <= nb <= ceiling

#level 1 => diff 0 => 0 à 10
#level 2 => diff 1 => 0 à 20
#level 3 => diff 2 => 0 à 30

def initInput() : 
    nom = input("Quel est votre nom ? ")
    #TODO Traitemenet du nom

# APRES
def playing(lvl) : 
    nb_essai = 3 + lvl * 2
    floor = 0
    ceiling = 10 + lvl * 10
    temps = 10
    nb_coup = 0
    randomChoice = randrange(floor, ceiling, 1)
    while True :
        nb_user = -1
        inputValid = False
        while (not inputValid) :
            nb_user = int(input("Entrez un nombre entre 1 et " + str(ceiling) + " :"))
            if is_valid(nb_user, floor, ceiling) :
                inputValid = True
            else :
                print("Erreur de saisie")
        nb_coup += 1
        if nb_user > randomChoice :
            print ('Votre nbre est trop grand')
        elif nb_user < randomChoice :
            print ('Votre nbre est trop petit')
        else :
            print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
            break

def main() :
    initInput()
    playing(int(input("Quel level voulez-vous ? (1 - 3) : ")))

main()



