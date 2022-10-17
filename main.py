from random import randrange
# nb_ordi =  randrange (1, 11, 1)
# if is_valid(nb_ordi, 1, 10) :
    
# print('Mon choix est = ', nb_ordi)

def is_valid(nb, floor, ceiling):
    return isinstance(nb, int) and floor <= nb <= ceiling :

#level 1 => diff 0 => 0 à 10
#level 2 => diff 1 => 0 à 20
#level 3 => diff 2 => 0 à 30

# nb_ordi = randrange(1,(10 * getlevel())+1,1)

diff = 1

def getLevel() : 
    global diff
    return diff

# APRES
def playing() : 
    global diff 
    nb_essai = 3 + diff * 2
    ceiling = 10 + diff * 10
    temps = 10
    nb_coup = 0
    while True :
        nb_user = -1
        while (not is_valid(nb_user = int(input ("Entrez SVP votre nombre ? "))))
            
        nb_coup += 1
        if nb_user > nb_ordi :
            print ('Votre nbre est trop grand')
        elif nb_user < nb_ordi :
            print ('Votre nbre est trop petit')
        else :
            print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
            break



