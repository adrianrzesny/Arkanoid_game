import pygame
import GameController
from Platform import Platform
from Ball import Ball
from Brick import Brick

pygame.init()
pygame.font.init()

#Creating a screen object, clock, background, font
screen = pygame.display.set_mode([GameController.WIDTH_SCREEN, GameController.HEIGHT_SCREEN])
clock = pygame.time.Clock()
image_background = pygame.image.load('images/background.png')
font = pygame.font.SysFont('Comic Sans MS', 24)

#Create a bricks objects
bricks = pygame.sprite.Group()
bricks = Brick.get_bricks(10, 7, GameController.level)

#Create a platform object
platform = Platform()
#Create a ball object
ball = Ball()

game_work = True
while game_work:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_work = False
            elif event.type == pygame.QUIT:
                game_work = False

    #Move platform
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platform.move_platform(-1)
    if keys[pygame.K_d]:
        platform.move_platform(1)
  
    #Check if all blocks have been destroyed
    if len(bricks.sprites()) == 0:
        GameController.level += 1
        if GameController.level >= 3:
            break
        ball.reset_position()
        platform.reset_position()
        bricks = Brick.get_bricks(10, 7, GameController.level)

    #Update objects
    bricks.update()
    ball.update(platform, bricks)
    platform.update()

    #Check if the ball touched the bottom edge
    if ball.defeat:
        GameController.hp -= 1
        if GameController.hp <= 0:
            break
        ball.reset_position()
        platform.reset_position()

    #Show background
    screen.blit(image_background, (0,0))

    #Show bricks
    for brick in bricks:
        screen.blit(brick.image, brick.position)

    #Show platform
    screen.blit(platform.image, platform.position)

    #Show ball
    screen.blit(ball.image, ball.position)

    #Show HP
    text_hp = font.render(f'HP: {GameController.hp}', False, (255, 255, 0))
    screen.blit(text_hp, (16, 16))
    
    text_level = font.render(f'Level: {GameController.level + 1}', False, (255, 255, 0))
    screen.blit(text_level, (920, 16))

    pygame.display.flip()
    clock.tick(30)


pygame.quit()