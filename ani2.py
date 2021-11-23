import pygame, sys
import time
class sjScenes(pygame.sprite.Sprite):
            def __init__(self, pos_x,pos_y):
                super().__init__()
                self.sprites = []
                self.is_animating = False
                self.sprites.append(pygame.image.load("assets\img\SJN\scene1\scene1.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene2\scene2.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene3\scene3p1.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene3\scene3p2.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene3\scene3p3.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene3\scene3p4.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene4\scene4p1.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene4\scene4p2.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene5\scene5p1.png"))
                self.sprites.append(pygame.image.load("assets\img\SJN\scene5\scene5p2.png"))
                self.current_sprite = 0
                self.image = self.sprites[self.current_sprite]
                self.rect = self.image.get_rect()
                self.rect.topleft = [pos_x, pos_y]
                
            def animate(self):
                self.is_animating = True
            
            def update(self):
                if self.is_animating == True:
                    self.current_sprite += 0.05
                    if self.current_sprite >= len(self.sprites):
                        self.current_sprite = 0
                        self.is_animating = False
                    self.image = self.sprites[int(self.current_sprite)]
                    
class pointer(pygame.sprite.Sprite):
    def __init__(self,pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.chalktap=pygame.mixer.Sound("assets/tap.mp3")
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
                if event.key==pygame.K_KP5:
                    sj_scene.animate()
        screen.blit(bg,(0,0))
        moving_scene.draw(screen)
        moving_scene.update()
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
bg = pygame.image.load("assets/chalkboard.jpg")
stage_select=pygame.image.load("stages-images/Anim-10.png")
firstcome_text=pygame.image.load("stages-images/Anim-02.png")
shortest_job_text=pygame.image.load("stages-images\Anim-03.png")
priority_text=pygame.image.load("stages-images\Anim-04.png")
shortest_time_text=pygame.image.load("stages-images\Anim-05.png")
select_num=pygame.image.load('stages-images/Anim-06.png')

#Pointer
pointer = pointer("assets/pointer.png")
pointer_group = pygame.sprite.Group()
pointer_group.add(pointer)

#scenes shortest jobs
screencenter =(200, 150)
moving_scene = pygame.sprite.Group()        
sj_scene = sjScenes(100,150)
moving_scene.add(sj_scene)

while True:
    game_state.state_manager()
    clock.tick(60)
