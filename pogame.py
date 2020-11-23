import pygame
from constants import *
from screen import create_screen, update_screen
from world import create_world, display_world, get_index
import random as rd

inventaire=[]

def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    return source, target
    

def main():
    # Création du "monde" tel que nous le définissons
    world = create_world()
    # Création des surfaces de dessin
    screen, background = create_screen(world)
    # Création d'une horloge
    clock = pygame.time.Clock()
    # Coordonnées [x, y] du joueur
    player = [rd.randint(0,WORLD_WIDTH), rd.randint(0,WORLD_HEIGHT)]
    
    #Coordonnées des objets :
  

    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    running = True

    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background, world, player)
    clock.tick()
    
    # Affichage d'un texte
    #font = pygame.font.Font(None, 18)
    #text = font.render("Appuyez sur T pour prendre un objet et sur G pour le poser.", 1, (255, 0, 255))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #textpos.centery = background.get_rect().centery
    #background.blit(text, textpos)

    # Blitter le tout dans la fenêtre
    #screen.blit(background, (0, 0))
    #pygame.display.flip()

    # Boucle "quasi" infinie, qui s'arrêtera si le joueur est mort, ou si l'arrêt du programme est demandé.
    while alive and running:
        # À chaque itération, on demande à pygame quels "évènements" se sont passés. Ces évènements sont l'interface
        # qui permet d'interragir avec l'extérieur du programme, et en particulier l'utilisateur (qui utilisera son
        # clavier, par exemple).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                
                # Une touche du clavier a été pressée.
                if event.key == pygame.K_q:
                    running = False
                     
            elif event.type == pygame.KEYUP:
                
                
                if event.key == pygame.K_RIGHT :
                    
                    if player[0] < WORLD_WIDTH-1:
                        player = (player[0]+1, player[1])
                        display_world(player, world, WORLD_WIDTH, WORLD_HEIGHT)

                        
                if event.key == pygame.K_LEFT :
                    if player[0] > 0:
                        player = (player[0]-1, player[1])
                        display_world(player, world, WORLD_WIDTH, WORLD_HEIGHT)

                        
                if event.key == pygame.K_UP :
                    if player[1] > 0 :
                        player = (player[0], player[1]-1)
                        display_world(player, world, WORLD_WIDTH, WORLD_HEIGHT)

                        
                if event.key == pygame.K_DOWN :
                    if player[1] < WORLD_HEIGHT-1:
                        player = (player[0], player[1]+1)
                        display_world(player, world, WORLD_WIDTH, WORLD_HEIGHT)
                        
                if event.key == pygame.K_p :
                    case = get_index(player[0], player[1])
                    print (case)
                    item = world[case]
                    transfer_item(world, inventaire, item)
                    
                
                                
        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background, world, player)
        
        clock.tick()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()


