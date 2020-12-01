import pygame
from constants import *
from screen import create_screen, update_screen
from world import create_world, display_world, get_index
import random as rd
import pygame_menu

pygame.init()
pygame.font.init()
pygame.mixer.init()
ZELDA1 = pygame.mixer.Sound('ZELDA 1.wav')
ZELDA2 = pygame.mixer.Sound('ZELDA 2.wav')
ZELDA3 = pygame.mixer.Sound('ZELDA 3.wav')
ZELDA4 = pygame.mixer.Sound('ZELDA 4.wav')
ZELDA5 = pygame.mixer.Sound('ZELDA 5.wav')
ZELDA6 = pygame.mixer.Sound('ZELDA 6.wav')
ZELDA7 = pygame.mixer.Sound('ZELDA 7.wav')
ZELDA8 = pygame.mixer.Sound('ZELDA 8.wav')



inventaire=[]
surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

fenetre = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

myfont = pygame.font.SysFont('Helvetic', 40)

def set_difficulté (valeur, difficulté):
    pass

            
def menu():
    menu = pygame_menu.Menu(500, 500, 'Bienvenue sur ',
                           theme=pygame_menu.themes.THEME_BLUE)
    menu.height=500
    menu_width=500

    menu.add_text_input('Pseudo :', default='Joueur 1')
    menu.add_selector('Difficulté :', [('Difficile', 1), ('Normal', 2), ('Facile', 3)], onchange=set_difficulté)
    menu.add_button('Jouer', jouer)
    menu.add_button('Quitter', pygame_menu.events.EXIT)

    menu.mainloop(surface)

def jouer():
    # Création du "monde" tel que nous le définissons

    world = create_world()
    
    ZELDA1.play()
    ZELDA2.play()
    ZELDA3.play()
    ZELDA4.play()
    ZELDA5.play()
    ZELDA6.play()
    ZELDA7.play()
    ZELDA8.play()
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
                break
            elif event.type == pygame.KEYDOWN:
                
                # Une touche du clavier a été pressée.
                if event.key == pygame.K_q:
                    running=False
                    
            elif event.type == pygame.KEYUP:
                
                
                if event.key == pygame.K_RIGHT :
                    
                    if player[0] < WORLD_WIDTH-1:
                        player = (player[0]+1, player[1])
                        index= get_index(player[0], player[1])
                        

                        
                if event.key == pygame.K_LEFT :
                    if player[0] > 0:
                        player = (player[0]-1, player[1])
                        index= get_index(player[0], player[1])

                        
                if event.key == pygame.K_UP :
                    if player[1] > 0 :
                        player = (player[0], player[1]-1)
                        index= get_index(player[0], player[1])


                        
                if event.key == pygame.K_DOWN :
                    if player[1] < WORLD_HEIGHT-1:
                        player = (player[0], player[1]+1)
                        index= get_index(player[0], player[1])
                        
                                           
        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background, world, player)
        
        clock.tick()
pass
    
        
menu()




