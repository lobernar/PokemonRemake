import pygame

def get_player_sprite(sheet, x, y, width, height):
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

def get_bill_sprite(sheet, x, y, width, height):
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite