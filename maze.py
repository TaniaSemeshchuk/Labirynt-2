#створи гру "Лабіринт"!
import pygame

win_width = 700
win_height = 500

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Лабіринт")
background = pygame.transform.scale(pygame.image.load("background.jpg"), 
                                    (win_width, win_height))

pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()

game = True
FPS = 60

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.blit(background,(0, 0))
    pygame.display.update()
    #pygame.clock.tick(FPS)


