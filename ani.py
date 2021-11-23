import pygame, sys


class pointer(pygame.sprite.Sprite):
    def __init__(self,pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.chalktap=pygame.mixer.Sound("tap.mp3")
    def update(self):
        self.rect.center=pygame.mouse.get_pos()
    def tap(self):
        self.chalktap.play()
class GameState():
    def __init__(self):
        self.state="intro"
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP1:
                    self.state="firstcome"
                if event.key==pygame.K_KP2:
                    self.state="shortest_job"
                if event.key==pygame.K_KP3:
                    self.state="priority"
                if event.key==pygame.K_KP4:
                    self.state="shortest_time"
                
        
        screen.blit(bg,(0,0))
        screen.blit(stage_select,(0,0))
        pygame.display.flip()


    def first_come(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(firstcome_text,(screen_width/2,screen_height/2))
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def shortest_job(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(shortest_job_text,(screen_width/2,screen_height/2))
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def priority(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(priority_text,(screen_width/2,screen_height/2))
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def shortest_time(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(shortest_time_text,(screen_width/2,screen_height/2))
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def state_manager(self):
        if self.state=='intro':
            self.intro()
        if self.state=='firstcome':
            self.first_come()
        if self.state=='shortest_job':
            self.shortest_job()
        if self.state=='priority':
            self.priority()
        if self.state=='shortest_time':
            self.shortest_time()



# General setup
pygame.init()
clock = pygame.time.Clock()
game_state=GameState()
# Game Screen
screen_width =800
screen_height =600 

screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load("chalkboard.jpg")
stage_select=pygame.image.load("anim-01.png")
firstcome_text=pygame.image.load("anim-02.png")
shortest_job_text=pygame.image.load("anim-03.png")
priority_text=pygame.image.load("anim-04.png")
shortest_time_text=pygame.image.load("anim-05.png")
pygame.mouse.set_visible(False)

#Pointer
pointer = pointer("chalk.png")
pointer_group = pygame.sprite.Group()
pointer_group.add(pointer)

while True:
    game_state.state_manager()
    clock.tick(60)
