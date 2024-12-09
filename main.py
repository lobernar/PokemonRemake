import pygame
from map import Map
from player import Player
from battle import Battle
from pokemon import Pokemon

SPEED = 100
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_W = 16
TILE_H = 16
# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# create initial map and player
map = Map(screen)
player = Player(screen, 100, 100)
map.add_player(player)

in_battle = True
pok1 = Pokemon()
pok2 = Pokemon()
battle = Battle(screen, [pok1, pok2])
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if(in_battle): battle.update()
    else: map.update()
    

    pygame.display.flip()
    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()