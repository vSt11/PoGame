import pygame

from constants import *


def create_screen(world):
    # Initialise screen
    pygame.init()
    board_width = WORLD_WIDTH * ROOM_SIZE
    board_height = WORLD_HEIGHT * ROOM_SIZE
    screen = pygame.display.set_mode((board_width, board_height))
    pygame.display.set_caption("Reconstitue la musique !")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    
    #blit layer
    layer = pygame.image.load ('map.png')
    layer = pygame.transform.scale(layer, (WORLD_WIDTH*ROOM_SIZE, WORLD_HEIGHT*ROOM_SIZE))
    background.blit(layer, (0, 0, WORLD_HEIGHT*ROOM_SIZE, WORLD_WIDTH*ROOM_SIZE))

    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            if bool(x % 2) == bool(y % 2):

                color = (200, 200, 200)
            else:
                color = (250, 250, 250)

            pygame.draw.rect(
                background,
                color,
                [
                    x * ROOM_SIZE,
                    y * ROOM_SIZE,
                    ROOM_SIZE,
                    ROOM_SIZE,
                ],
            )

    return screen, background


def update_screen(screen, background, world, player):
    player_x, player_y = player
    screen.blit(background, (0, 0))

    # couleur (red, green, blue)
    pygame.draw.rect(
        screen,
        (224, 64, 64),
        [
            player_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
            player_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
            PLAYER_SIZE,
            PLAYER_SIZE,
        ],
    )

    # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...

    pygame.display.flip()
