import pygame
import copy
import GameController

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        super(Brick, self).__init__()
        self.image_orginal = pygame.image.load('images/brick.png')
        self.position = pygame.Rect(x, y, 96, 48)
        self.health = health

    def update_brick(self):
        color_mask = 0
        if self.health == 3:
            color_mask = (128,0, 0)
        if self.health == 2:
            color_mask = (0, 0, 128)
        if self.health == 1:
            color_mask = (0, 128, 0)
        
        self.image = copy.copy(self.image_orginal)
        self.image.fill(color_mask, special_flags=pygame.BLEND_ADD)

    def update(self):
        self.update_brick()

    def hit(self):
        self.health -=1
        if self.health <= 0:
            self.kill()
    
    def get_bricks(level):
        bricks = pygame.sprite.Group()
        load_level = None
        if level == 0:
            load_level = GameController.LEVEL_1
        if level == 1:
            load_level = GameController.LEVEL_2
        if level == 2:
            load_level = GameController.LEVEL_3
     
        for i in range(0, len(load_level)):
            for j in range(0, len(load_level[i])):
                if load_level[i][j] != 0:
                    brick = Brick(32+j*96, 32+i*48, load_level[i][j])
                    bricks.add(brick)

        return bricks 