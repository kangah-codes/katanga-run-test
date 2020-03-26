import pygame, random, math
from settings import *
from required import *
pygame.init()

def getSpriteByPosition(position, group):
            try:
                return group.sprites()[position]
            except IndexError:
                pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = {
            "idle": Animation([
                "png/Idle__000.png",
                "png/Idle__001.png",
                "png/Idle__002.png",
                "png/Idle__003.png",
                "png/Idle__004.png",
                "png/Idle__005.png",
                "png/Idle__006.png",
                "png/Idle__007.png",
                "png/Idle__008.png",
                "png/Idle__009.png",
            ], 200, True),
            "run": Animation([
                "png/Run__000.png",
                "png/Run__001.png",
                "png/Run__002.png",
                "png/Run__003.png",
                "png/Run__004.png",
                "png/Run__005.png",
                "png/Run__006.png",
                "png/Run__007.png",
                "png/Run__008.png",
                "png/Run__009.png",
            ], 200, True)
        }
        self.position = vector(206, HEIGHT/2)
        self.acceleration = vector(0, 0)
        self.velocity = vector(0, 0)
        self.scale = scale
        self.state = self.image["run"]
        self.rect = self.state.get_rect()

    def update(self):
        self.state.update(60)
        self.state.get_mask()
        self.rect.midbottom = self.position

    def draw(self, screen):
        img = pygame.transform.flip(self.state.getScaledImage(self.scale), 0, 0)
        screen.blit(img, (self.position.x, self.position.y))


class Tile(pygame.sprite.Sprite):
    def __init__(self, ground, type=None):
        pygame.sprite.Sprite.__init__(self)
        self.ground = ground
        self.type = type
        if self.type != "acid":
            self.image = pygame.transform.scale(pygame.image.load("Tiles/BGTile (2).png"), (tileWidth, tileHeight))
        elif self.type == "acid":
            self.image = pygame.transform.scale(pygame.image.load("Tiles/Acid (1).png"), (tileWidth, tileHeight))
        self.rx = 0
        self.rect = self.image.get_rect()
        self.position = vector(WIDTH, HEIGHT - self.rect.height)

    def update(self, dt):
        self.rect.midbottom = self.position
        self.position.x -= 5
        if self.position.x + self.rect.width < 0 and self.type != 'acid':
            if random.randint(0, 10) < self.ground.acid_tile_occurance:
                if not self.contains_acid():
                    acid = Tile(HEIGHT, type='acid')
                    self.ground.add(acid)
            self.position.x = len(self.ground.ground_tiles) * (self.rect.width)+ self.position.x
            # print self.position.x, len(self.ground.ground_tiles)
        if self.position.x + self.rect.width < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.position.x + (self.rect.width * self.rx), self.position.y))

    def contains_acid(self):
        for t in self.ground.ground_tiles:
            if t.type == 'acid':
                return True
        return False

class Ground(pygame.sprite.Sprite):
    def __init__(self, acid=100):
        pygame.sprite.Sprite.__init__(self)
        self.ground_tiles = SpriteGroup()
        x = 0
        cx = 0
        self.acid_tile_occurance = acid
        while True:
            t = Tile(self, HEIGHT)
            t.position.x, t.position.y = t.rect.width * x, HEIGHT - t.rect.height
            cx = t.position.x
            if cx > WIDTH + t.rect.width:
                break
            else:
                self.ground_tiles.add(t)
            x += 1


    def add(self, tile):
        tile.position.x, tile.position.y = tile.rect.width * (len(self.ground_tiles.sprites()) - 1), HEIGHT - tile.rect.height
        self.ground_tiles.add(tile)

    def get_rect(self):
        for tile in self.ground_tiles:
            print tile

    def update(self, dt):
        self.ground_tiles.update(dt)

    def draw(self, screen):
        self.ground_tiles.draw(screen)
