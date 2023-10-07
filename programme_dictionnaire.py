#Lien du sujet : https://www.codingame.com/ide/puzzle/don't-panic-episode-1

'''
Méthode de résolution :
    - 1/ Optimale : Utilisation d'un dictionnaire
    - 2/ Brute Force : Utilisation d'une liste
'''

#METHODE 1 - OPTIMALE

#width : longueur de l'axe X c-à-d de l'étage
#nb_round : nb de tours maximum pour résoudre le problème
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevator_floor, elevator_pos = exit_floor,exit_pos
dict_floor_pos = {exit_floor:exit_pos} #Dictionnaire de couple étage/sortie

for i in range(nb_elevators): #Remplissage du dictionnaire
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    dict_floor_pos[elevator_floor] = elevator_pos

while True:
    inputs = input().split() #Les 2 inputs sont l'étage du clone et sa position sur un axe X
    clone_floor, clone_pos = int(inputs[0]),int(inputs[1]) #Etage et Position du clone
    direction = inputs[2]  #Direction du clone leader: LEFT or RIGHT

    if direction == "NONE":
        print("WAIT")
        continue

    elevator_pos = dict_floor_pos[clone_floor]
    dist_asc_clone = elevator_pos - clone_pos

    #Si dist_asc_clone > 0 : l'ascenseur est positionné à droite du clone
    #Si la direction du clone est "LEFT" : il faut que le premier clone s'arrête car il est dans le mauvais sens
    if (((dist_asc_clone > 0) and (direction=="LEFT")) or 
    ((dist_asc_clone < 0) and (direction=="RIGHT"))):
        print("BLOCK")
    else:
        print("WAIT")


"""
#METHODE 2 -BRUTE FORCE

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevator_floor, elevator_pos = exit_floor,exit_pos
L_elevator_floor_and_pos = [[exit_floor,exit_pos]]

for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    L_elevator_floor_and_pos.append([elevator_floor, elevator_pos])

while True:
    inputs = input().split()
    clone_floor, clone_pos = int(inputs[0]),int(inputs[1])    
    direction = inputs[2]
    for couple in L_elevator_floor_and_pos:
        if couple[0] == clone_floor:
            elevator_pos = couple[1]
            break

    dist_asc_clone = elevator_pos - clone_pos

    if (((dist_asc_clone > 0) and (direction=="LEFT")) or 
    ((dist_asc_clone < 0) and (direction=="RIGHT"))):
        print("BLOCK")
    else:
        print("WAIT")
"""
