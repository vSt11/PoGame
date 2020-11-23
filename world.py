import random as rd
from constants import *

def display_world(joueur, world, hauteur, largeur):
    print("\n")
    for y in range (hauteur):
        for x in range(largeur) :
            if joueur == (x,y):           
                print("[X]", end="")
            else :
                print('[ ]', end="")
    print()

def create_world():
    available_items = ["lampe", "", "épée", "arc", "",  "monstre", "trou","",  "bombe", "champignon", "étoile", ""]
    inventaire = []
    world=[]
    for y in range(WORLD_HEIGHT):
        for x in range (WORLD_WIDTH):
            inventaire.insert(x, rd.choices(available_items, k=1))
            world.append(inventaire[x])
        case=get_index(x,y)
        print (case)
        print(world[case])
        
    return world, inventaire, case

def get_index(x, y):
    return y*WORLD_HEIGHT+x
