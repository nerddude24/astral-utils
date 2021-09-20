import pygame


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Add(self, other):
        self.x += other.x
        self.y += other.y

    def Sub(self, other):
        self.x -= other.x
        self.y -= other.y

    def Multiply(self, other):
        self.x *= other.x
        self.y *= other.y

    def get(self):
        return (self.x, self.y)


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: Vector2, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("black")
        self.rect = self.image.get_rect(topleft=pos.get())

    def update(self, x_shift):
        self.rect.x += x_shift
