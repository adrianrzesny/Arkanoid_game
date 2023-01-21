import pygame
import GameController

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.image = pygame.image.load('images/pad.png')
        self.move = 0
        self.reset_position()

    def reset_position(self):
        self.position = pygame.Rect(GameController.WIDTH_SCREEN/2-70, GameController.HEIGHT_SCREEN-100, 140, 30)
    
    def move_platform(self, value):
        speed = 10
        self.position.move_ip(value*speed, 0)
        self.move = value
        if self.position.left <= 0: self.position.x = 0
        if self.position.right >= GameController.WIDTH_SCREEN: self.position.x = GameController.WIDTH_SCREEN - 140
    
    def update(self):
        self.move = 0