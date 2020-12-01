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
    available_items = ["ZELDA1", "ZELDA2", "ZELDA3", "ZELDA4", "ZELDA5", "ZELDA6", "ZELDA7", "ZELDA8"]
    contenu = []
    world=[]
    for y in range(WORLD_HEIGHT):
        for x in range (WORLD_WIDTH):
            contenu.insert(x, rd.choices(available_items, k=3))
            world.append(contenu[x])
    case=get_index(x,y)
        
    print(world[case])
        
    return world

def get_index(x, y):
    return (y*WORLD_WIDTH+x)
