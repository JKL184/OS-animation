import pygame, sys
# General setup

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.chalktap=pygame.mixer.Sound("tap.mp3")
    def update(self):
        self.rect.center=pygame.mouse.get_pos()
    def tap(self):
        self.chalktap.play()

pygame.init()
clock = pygame.time.Clock()
# Game Screen
screen_width =800
screen_height =600 

screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load("chalkboard.jpg")

crosshair = Crosshair("chalk.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.tap()
    pygame.display.flip()
    screen.blit(bg,(0,0))
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
