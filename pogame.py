import pygame
from constants import *
from screen import create_screen, update_screen
from world import create_world, get_index
import random as rd
import pygame_menu
import time

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
ZELDAFINAL = pygame.mixer.Sound('ZELDAFINAL.wav')
DIE = pygame.mixer.Sound('die.wav')
GAGNE = pygame.mixer.Sound('fan2.wav')
MENU = pygame.mixer.Sound('MENU.wav')


inventaire=[]
surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

fenetre = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

myfont = pygame.font.SysFont('Helvetic', 40)


def son_facile(player) :
    if player == (2,1) :
        ZELDA1.play()
    elif player== (3,1) :
        ZELDA2.play()
    elif(player) == (4,1) :
        ZELDA3.play()
    elif(player) == (4, 2) :
        ZELDA4.play()
    elif player==(4,3) :
        ZELDA5.play()
    elif player==(3,3) :
        ZELDA6.play()
    elif player==(3,4):
        ZELDA7.play()
    elif player==(3,5):
        ZELDA8.play()
    elif player==(4,5):
        GAGNE.play()
        return player

def gagne(background, screen) :
    font = pygame.font.Font(None, 80)
    text = font.render("Gagné !!!!", 1, (255, 0, 255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    #Blitter le tout dans la fenêtre
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    menu()

def perdu(background, screen) :
    DIE.play()
    font = pygame.font.Font(None, 22)
    text = font.render("Perdu !", 1, (255, 0, 255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    #Blitter le tout dans la fenêtre
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    jouer()
    
            
def menu():
    menu = pygame_menu.Menu(600, 500, 'Bienvenue sur mon jeu',
                           theme=pygame_menu.themes.THEME_BLUE)
    menu.height=500
    menu_width=500

    menu.add_text_input('Pseudo :', default='Link')
    menu.add_selector('Difficulté :', [('Difficile', 1), ('Normal', 2), ('Facile', 3)])
    menu.add_button('Jouer', jouer)
    menu.add_button('Quitter', pygame_menu.events.EXIT)

    menu.mainloop(surface)

def jouer():
    # Création du "monde" tel que nous le définissons

    world = create_world()
    
    # Création des surfaces de dessin
    screen, background = create_screen(world)
    # Création d'une horloge
    clock = pygame.time.Clock()
    # Coordonnées [x, y] du joueur
    player = [2, 2]
    
    #Coordonnées des objets :
  

    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    global running
    running = True
    


    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background, world, player)
    clock.tick()
     
    # Affichage d'un texte
 

    # Boucle "quasi" infinie, qui s'arrêtera si le joueur est mort, ou si l'arrêt du programme est demandé.
    while alive and running:
        # À chaque itération, on demande à pygame quels "évènements" se sont passés. Ces évènements sont l'interface
        # qui permet d'interragir avec l'extérieur du programme, et en particulier l'utilisateur (qui utilisera son
        # clavier, par exemple).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MENU.play()
                menu()
            elif event.type == pygame.KEYDOWN:
                
                # Une touche du clavier a été pressée.
                if event.key == pygame.K_q:
                    MENU.play()
                    menu()
                    
                #if player != (0,0) or 
                    
            elif event.type == pygame.KEYUP:
                
                
                if event.key == pygame.K_RIGHT :
                    
                    if player[0] < WORLD_WIDTH-1:
                        player = (player[0]+1, player[1])
                        index= get_index(player[0], player[1])
                        print(player)
                        son_facile(player)
                        if player != (2,2) and player!=(2,1) and player!=(3,1) and player!=(4,1) and player!=(4,2) and player!=(4,3) and player!=(3,3) and player!=(3,4) and player!=(3,5) and player!=(4,5) :
                            perdu(background, screen)
                            player = (2,2)
                        
                        
                if event.key == pygame.K_LEFT :
                    if player[0] > 0:
                        player = (player[0]-1, player[1])
                        index= get_index(player[0], player[1])
                        print(player)
                        son_facile(player)
                        if player != (2,2) and player!=(2,1) and player!=(3,1) and player!=(4,1) and player!=(4,2) and player!=(4,3) and player!=(3,3) and player!=(3,4) and player!=(3,5) and player!=(4,5) :
                            perdu(background, screen)
                            player = (2,2)
                        
                if event.key == pygame.K_UP :
                    if player[1] > 0 :
                        player = (player[0], player[1]-1)
                        index= get_index(player[0], player[1])
                        print(player)
                        son_facile(player)
                        if player != (2,2) and player!=(2,1) and player!=(3,1) and player!=(4,1) and player!=(4,2) and player!=(4,3) and player!=(3,3) and player!=(3,4) and player!=(3,5) and player!=(4,5) :
                            perdu(background, screen)
                            player = (2,2)

                        
                if event.key == pygame.K_DOWN :
                    if player[1] < WORLD_HEIGHT-1:
                        player = (player[0], player[1]+1)
                        index= get_index(player[0], player[1])
                        print(player)
                        son_facile(player)
                        
                        if player != (2,2) and player!=(2,1) and player!=(3,1) and player!=(4,1) and player!=(4,2) and player!=(4,3) and player!=(3,3) and player!=(3,4) and player!=(3,5) and player!=(4,5) :
                            perdu(background, screen)
                            player = (2,2)
                        
                                           
        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background, world, player)
        if player == (4,5) :
            gagne(background, screen)
        time.sleep(0.1)
        
        clock.tick()
pass
    
        
menu()




