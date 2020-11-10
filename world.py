import random


def create_world(width=None, height=None):
    # Si la largeur n'est pas définie, on en choisit une au hasard
    if not width or width < 0:
        width = random.randint(8, 16)

    # Si la hauteur n'est pas définie, on en choisit une au hasard
    if not height or height < 0:
        height = random.randint(8, 12)

    world = []

    # TODO Il faut remplir notre terrain ici, en fonction de la taille choisie préalablement.

    return world
