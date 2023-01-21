import pygame
import random
import GameController

vec = pygame.math.Vector2

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.image = pygame.image.load('images/ball.png')
        self.reset_position()
        self.r = 16
        self.defeat = False
    
    def reset_position(self):
        self.coordinates = vec(GameController.WIDTH_SCREEN/2, GameController.HEIGHT_SCREEN-140)
        self.position = self.image.get_rect(center=self.coordinates)
        self.vector = vec(0, -10)
        self.angle_inclination = random.randrange(-30, 30)
        self.vector.rotate_ip(self.angle_inclination)
        self.defeat = False

    def update(self, platform, bricks):
        self.coordinates += self.vector
        self.position.center = self.coordinates
        self.check_collision(platform, bricks)

    def check_collision(self, platform, bricks):

        #The edges of the screen
        if self.position.x <= 0:
            self.vector.x *= -1
        if self.position.right >= GameController.WIDTH_SCREEN:
            self.vector.x *= -1
        if self.position.top<= 0:
            self.vector.y *= -1
        if self.position.bottom >= GameController.HEIGHT_SCREEN:
            self.defeat = True
        
        #Platform
        if self.position.colliderect(platform.position):
            self.vector.y *= -1
            self.vector.x += platform.move * 2
            if self.vector.x < -10: self.vector.x = -10
            if self.vector.x > 10: self.vector.x = 10
         
        #Bricks
        for brick in bricks:
            if self.collision_with_brick(self, brick):
                brick.hit()
                break
        
    def collision_with_brick(self, ball, brick):
        distance_x = abs(ball.position.centerx - brick.position.centerx) - brick.position.w / 2
        distance_y = abs(ball.position.centery - brick.position.centery) - brick.position.h / 2

        if distance_x < ball.r and distance_y < ball.r:
            if distance_x < distance_y:
                self.vector.y *= -1
            else:
                self.vector.x *= -1
            return True
        return False