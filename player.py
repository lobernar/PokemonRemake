import pygame

SPEED = 1
ANIMATION_DELAY = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.pokemons = []
        self.name = ''
        self.money = 0
        self.screen = screen
        self.player_sprites = None
        self.rect = None
        self.image = None
        self.sprites = {}  # Dictionary to store movement sprites
        self.step = 1
        self.last_dir = None
        self.animation_counter = 0
        self.load_sprites()

    def load_sprites(self):
        # Load sprites and store them in the dictionary
        self.player_sprites = pygame.image.load('sprites/PlayerSprites.png').convert_alpha()
        directions = ['down', 'up', 'left', 'right']
        y_positions = [42, 75, 108, 141]  # Corresponding y-coordinates for each direction

        for direction, y in zip(directions, y_positions):
            self.sprites[direction] = [
                self.get_player_sprite(self.player_sprites, 8 + i + i * 16, y, 16, 32) 
                for i in range(3)
            ]

        self.last_dir = self.sprites['down'][1]
        self.image = self.last_dir
        self.rect = self.image.get_rect()

    def get_player_sprite(self, sheet, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)  # Transparent background
        sprite.set_colorkey((255, 127, 39))
        sprite.blit(sheet, (0, 0), (x, y, width, height))
        return sprite

    def move(self):
        # Movement logic
        keys = pygame.key.get_pressed()
        direction = None

        if keys[pygame.K_w]:  # Move up
            direction = 'up'
            self.y -= SPEED
        elif keys[pygame.K_s]:  # Move down
            direction = 'down'
            self.y += SPEED
        elif keys[pygame.K_a]:  # Move left
            direction = 'left'
            self.x -= SPEED
        elif keys[pygame.K_d]:  # Move right
            direction = 'right'
            self.x += SPEED

        if direction:
            self.animation_counter += 1
            if self.animation_counter > ANIMATION_DELAY:
                self.animation_counter = 0
                self.step += 1  # Cycle through sprite frames
                self.step = self.step % 3

            self.image = self.sprites[direction][self.step]
            self.last_dir = self.image  # Update last direction
        else: self.animation_counter = 0

        self.rect = self.image.get_rect(midbottom=(self.x, self.y))


    def update(self):
        self.move()
        #self.screen.blit(self.image, (self.x, self.y))