import pygame

def get_sprite(sheet, x, y, width, height):
    """Extracts a sprite from the sprite sheet.
    
    Args:
        sheet: The loaded sprite sheet.
        x, y: The top-left coordinates of the sprite on the sheet.
        width, height: The dimensions of the sprite.
    
    Returns:
        A Pygame surface containing the sprite.
    """
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)  # Transparent background
    sprite.set_colorkey((255, 127, 39))
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite
# pygame setup

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_sprites = pygame.image.load('sprites/PlayerSprites.png').convert_alpha()
sprite = get_sprite(player_sprites, 8, 42, 16, 32)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0,0,0))
    screen.blit(sprite, (100, 100))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()