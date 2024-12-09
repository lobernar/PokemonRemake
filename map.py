import pytmx
import pyscroll
from player import Player

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.tmx = None
        self.group = None
        self.map_layer = None
        self.player = None
        self.switch_map(r'maps\gracidea-main\maps\all\worldmap')

    def switch_map(self, map):
        self.tmx = pytmx.load_pygame(r'maps\gracidea-main\maps\hoenn\littleroot-town.tmx', pixelalpha=True)
        # Debug transparency issues
        for layer in self.tmx.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image:
                        image.set_colorkey((255, 255, 255))  # Remove white background
        map = pyscroll.data.TiledMapData(self.tmx)
        self.map_layer = pyscroll.BufferedRenderer(map, self.screen.get_size())
        self.map_layer.zoom = 4
        self.group = pyscroll.PyscrollGroup(self.map_layer)

    def add_player(self, player : Player):
        self.player = player
        self.group.add(player, layer=1)

    def update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)