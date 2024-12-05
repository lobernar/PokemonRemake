import pygame
from functs import get_player_sprite

SPEED = 100
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = [100, 100] # (x, y) position of player

# load sprites
player_sprites = pygame.image.load('sprites/PlayerSprites.png').convert_alpha()
downs = [get_player_sprite(player_sprites, 8+i+i*16, 42, 16, 32) for i in range(3)]
ups = [get_player_sprite(player_sprites, 8+i+i*16, 75, 16, 32) for i in range(3)]
lefts = [get_player_sprite(player_sprites, 8+i+i*16, 108, 16, 32) for i in range(3)]
rights = [get_player_sprite(player_sprites, 8+i+i*16, 141, 16, 32) for i in range(3)]
step = 1
last_dir = downs[step]

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')
    screen.blit(last_dir, player_pos)
    
    # Movement logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        step = step % 2
        step += 1
        player_pos[1] -= SPEED * dt
        last_dir = ups[step]
    if keys[pygame.K_s]:
        step = step % 2
        step += 1
        player_pos[1] += SPEED * dt
        last_dir = downs[step]
    if keys[pygame.K_a]:
        step = step % 2
        step += 1
        player_pos[0] -= SPEED * dt
        last_dir = lefts[step]
    if keys[pygame.K_d]:
        step = step % 2
        step += 1
        player_pos[0] += SPEED * dt
        last_dir = rights[step]

    # Neutral step
    #step = 1

    pygame.display.flip()
    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()