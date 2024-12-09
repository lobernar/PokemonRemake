import pygame
from pokemon import Pokemon

class Battle:
    def __init__(self, screen, pokemons : list):
        #pygame.key.set_repeat(120, 70)
        self.pokemons = pokemons
        self.screen = screen
        self.font = pygame.font.Font(r'fonts\Grand9KPixel.ttf', 30)
        self.selected_action = 'Fight'
        self.arrow = pygame.image.load('sprites/selectArrow.png')
        self.arrow = pygame.transform.scale(self.arrow, (45, 45))
        self.arrow_rect = self.arrow.get_rect()
        self.arrow_pos = [self.screen.get_width()/2 + 25, 570]
        self.pos_fight = [self.screen.get_width()/2 + 25, 570]
        self.pos_bag = [self.screen.get_width() / 2 + 325, 570]
        self.pos_run = [self.screen.get_width() / 2 + 325, 640]
        self.pos_pokemon = [self.screen.get_width() / 2 + 25, 640]
        self.draw_ui()
        self.finished = False

    def draw_ui(self):
        pok1_rect = pygame.Surface((300, 100))
        pok1_rect.fill('white')
        pok2_rect = pygame.Surface((300, 100))
        pok2_rect.fill('white')
        self.draw_background()
        self.draw_poke_stats(self.pokemons[0], pok1_rect)
        self.draw_poke_stats(self.pokemons[1], pok2_rect)
        self.screen.blit(pok1_rect, (80,30))
        self.screen.blit(pok2_rect, (980, 400))
        self.draw_action_menu()
        self.screen.blit(self.arrow, self.arrow_pos)

    def draw_poke_stats(self, pokemon, surface):
        health_bar_width = 150
        remaining_health = pokemon.hp / pokemon.max_hp
        lost_health = 1 - remaining_health

        color = 'green'
        if(0.2 < remaining_health <= 0.5): color = 'yellow'
        elif(remaining_health <=0.2): color = 'red'

        remaining_health_rect = pygame.Surface((health_bar_width*remaining_health, 20))
        lost_health_rect = pygame.Surface((lost_health * 150, 20))  # Width based on lost health
        lost_health_rect.fill('white')
        health_bar = pygame.Surface((154, 24))
        remaining_health_rect.fill(color)

        # Draw the remaining health and lost health
        health_bar.blit(lost_health_rect, (2 + remaining_health_rect.get_width(), 2))
        health_bar.blit(remaining_health_rect, (2, 2))  

        # Text
        hp_text = self.font.render(f'{pokemon.hp} / {pokemon.max_hp}', True, 'black')
        name_text = self.font.render(f'{pokemon.name}', True, 'black')

        # Draw health bar on surface
        pos_x, pos_y = surface.get_width(), surface.get_height()
        x = pos_x - 170
        y = pos_y - 40
        surface.blit(health_bar, (x, y))
        surface.blit(hp_text, (x + 30, y+4))
        surface.blit(name_text, (3, 3))

    def draw_background(self):
        background_sprites = pygame.image.load('sprites/BattleBackgrounds.png')
        background = self.get_sprite(background_sprites, 6, 6, 240, 110)
        background = pygame.transform.scale(background,(self.screen.get_width(), self.screen.get_height()-205))
        self.screen.blit(background, (0, 0))
    
    def draw_action_menu(self):
        bottom_background = pygame.image.load('sprites/bottom_battlebg.png')
        player_actions = pygame.image.load('sprites/player_actions_battle.png')
        bottom_background = pygame.transform.scale(bottom_background, (self.screen.get_width(), 200))
        player_actions = pygame.transform.scale(player_actions, (self.screen.get_width()/2, 180))
        font = pygame.font.Font(r'fonts\Grand9KPixel.ttf', 50)
        text = font.render(f"What will {self.pokemons[1].name} do?", True, 'white')
        
        self.screen.blit(bottom_background, (0, 520))
        self.screen.blit(player_actions, (self.screen.get_width()/2, 530))
        self.screen.blit(text, (60, 575))

    def get_sprite(self, sheet, x, y, width, height):
        sprite = pygame.Surface((width, height))  # Transparent background
        sprite.blit(sheet, (0, 0), (x, y, width, height))
        return sprite

    def move_arrow(self, event):
        if event.type == pygame.QUIT: 
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            # Define movement transitions
            transitions = {
                'w': {'Fight': 'Pokemon', 'Pokemon': 'Fight', 'Run': 'Bag', 'Bag': 'Run'},
                's': {'Fight': 'Pokemon', 'Pokemon': 'Fight', 'Run': 'Bag', 'Bag': 'Run'},
                'a': {'Fight': 'Bag', 'Bag': 'Fight', 'Pokemon': 'Run', 'Run': 'Pokemon'},
                'd': {'Fight': 'Bag', 'Bag': 'Fight', 'Pokemon': 'Run', 'Run': 'Pokemon'}
            }

            # Map the arrow positions to actions
            arrow_positions = {
                'Fight': self.pos_fight,
                'Pokemon': self.pos_pokemon,
                'Bag': self.pos_bag,
                'Run': self.pos_run
            }

            # Detect the key press and adjust the selection
            key_to_action = {
                pygame.K_w: 'w',
                pygame.K_s: 's',
                pygame.K_a: 'a',
                pygame.K_d: 'd'
            }

            if event.key in key_to_action:
                key = key_to_action[event.key]
                self.selected_action = transitions[key][self.selected_action]
                self.arrow_pos = arrow_positions[self.selected_action]

            print(self.selected_action)

    def update(self):
        # Draw UI components and the arrow
        self.draw_ui()  # Ensure you redraw everything here
        # Process events
        for event in pygame.event.get():
            self.move_arrow(event)
