import pygame
import pygame_menu

pygame.init()

surface = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

def menu(): 
    menu = pygame_menu.Menu(300, 400, 'Bienvenue sur ',
                           theme=pygame_menu.themes.THEME_BLUE)

    menu.add_text_input('Pseudo :', default='Joueur 1')
    menu.add_selector('Difficulté :', [('Difficile', 1), ('Normal', 2), ('Facile', 3)], onchange=set_difficulty)
    menu.add_button('Jouer', start_the_game)
    menu.add_button('Quitter', pygame_menu.events.EXIT)

    menu.mainloop(surface)
