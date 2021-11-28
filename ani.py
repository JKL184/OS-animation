import pygame
import sys
import os


class pointer(pygame.sprite.Sprite):
    def __init__(self, pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.chalktap = pygame.mixer.Sound("assets/tap.mp3")

    def update(self,):
        self.rect.center = pygame.mouse.get_pos()

    def tap(self):
        self.chalktap.play()


class option(pygame.sprite.Sprite):
    def __init__(self, x, y, pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect(center=(x, y))


class sjScenes(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load(
            r"assets/img/SJN/scene1/scene1.png"))
        self.sprites.append(pygame.image.load(
            r"assets/img/SJN/scene2/scene2.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/SJN/scene3/scene3p1.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/SJN/scene3/scene3p2.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/SJN/scene3/scene3p3.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/SJN/scene3/scene3p4.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/SJN/scene4/scene4p1.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/SJN/scene4/scene4p2.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/SJN/scene5/scene5p1.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/SJN/scene5/scene5p2.png"))
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


class priorityScenes(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-1.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-2.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-3.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-4.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-5.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-6.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-7.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-8.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-9.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-10.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-11.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-12.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-13.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-14.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-15.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-16.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-17.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-18.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-19.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-20.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-21.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-22.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-23.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-24.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-25.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-26.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-27.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-28.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-29.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-30.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-31.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-32.png"))
        self.sprites.append(pygame.image.load(
            "assets/img/priority/scene1-33.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.035
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]



class fcfsScenes(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-01.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-02.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-03.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-04.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-05.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-06.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-07.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-08.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-09.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-10.jpg"))
        self.sprites.append(pygame.image.load(
            "assets/img/fcfs/FCFS-11.jpg"))
        
       

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.035
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]


class GameState():
    def __init__(self):
        self.state = "intro"

    def intro(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    self.state = "firstcome"
                if event.key == pygame.K_KP2:
                    self.state = "shortest_job"
                if event.key == pygame.K_KP3:
                    self.state = "priority"
                if event.key == pygame.K_KP4:
                    self.state = "shortest_time"
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist = [opt1, opt2, opt3, opt4]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts) > 0:
                    if clicked_opts[0] == opt1:
                        self.state = "firstcome"
                    elif clicked_opts[0] == opt2 and len(clicked_opts) > 0:
                        self.state = "shortest_job"
                    elif clicked_opts[0] == opt3 and len(clicked_opts) > 0:
                        self.state = "priority"
                    elif clicked_opts[0] == opt4 and len(clicked_opts) > 0:
                        self.state = "shortest_time"

        screen.blit(bg, (0, 0))
        screen.blit(stage_select, (200, 10))
        screen.blit(select_num, (200, 300))
        option_group.draw(screen)
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def first_come(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist = [barrow]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts) > 0:
                    if clicked_opts[0] == barrow:
                        fcfs.is_animating= False
                        self.state = "intro"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP0:
                    self.state = "intro"
                if event.key == pygame.K_KP1:
                    fcfs.animate()

        screen.blit(bg, (0, 0))
        arrow_group.draw(screen)
        screen.blit(firstcome_text, (200, 0))
        moving_scene1.draw(screen)
        moving_scene1.update()
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def shortest_job(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()

                pos = pygame.mouse.get_pos()
                optlist = [barrow]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts) > 0:
                    if clicked_opts[0] == barrow:
                        sj_scene.is_animating = False
                        self.state = "intro"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP0:
                    self.state = "intro"
                if event.key == pygame.K_KP5:
                    sj_scene.animate()

        screen.blit(bg, (0, 0))
        arrow_group.draw(screen)
        screen.blit(shortest_job_text, (200, 0))
        moving_scene.draw(screen)
        moving_scene.update()
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    
    
    def priority(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist = [barrow]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts) > 0:
                    if clicked_opts[0] == barrow:
                        priority.is_animating = False
                        self.state = "intro"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.state = "intro"
                if event.key == pygame.K_d:
                    priority.animate()

        screen.blit(bg, (0, 0))
        arrow_group.draw(screen)
        screen.blit(priority_text, (200, 0))
        moving_scene2.draw(screen)
        moving_scene2.update()
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def shortest_time(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist = [barrow]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts) > 0:
                    if clicked_opts[0] == barrow:
                        self.state = "intro"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP0:
                    self.state = "intro"

        screen.blit(bg, (0, 0))
        screen.blit(shortest_time_text, (screen_width/2, screen_height/2))
        arrow_group.draw(screen)
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'firstcome':
            self.first_come()
        if self.state == 'shortest_job':
            self.shortest_job()
        if self.state == 'priority':
            self.priority()
        if self.state == 'shortest_time':
            self.shortest_time()


# General setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()
# Game Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load("assets/chalkboard.jpg")
# background = pygame.Surface(screen.get_size())
# background = background.convert()
# background.fill()

# Game options
stage_select = pygame.image.load('stages-images/Anim-01.png')
firstcome_text = pygame.image.load("stages-images/Anim-02.png")
shortest_job_text = pygame.image.load("stages-images/Anim-03.png")
priority_text = pygame.image.load("stages-images/Anim-04.png")
shortest_time_text = pygame.image.load("stages-images/Anim-05.png")
select_num = pygame.image.load('stages-images/Anim-06.png')
pygame.mouse.set_visible(False)

# Pointer
pointer = pointer("assets/pointer.png")
pointer_group = pygame.sprite.Group()
pointer_group.add(pointer)

# Back Arrow
barrow = option(60, 40, "assets/arrow.png")
arrow_group = pygame.sprite.Group([barrow])
# Stage options
opt1 = option(230, 100, "stages-images/Anim-02.png")
opt2 = option(200, 150, "stages-images/Anim-03.png")
opt3 = option(200, 200, "stages-images/Anim-04.png")
opt4 = option(230, 250, "stages-images/Anim-05.png")
option_group = pygame.sprite.Group([opt1, opt2, opt3, opt4])

# scenes shortest jobs
screencenter = (200, 150)
moving_scene = pygame.sprite.Group()
moving_scene1 = pygame.sprite.Group()
moving_scene2 = pygame.sprite.Group()
sj_scene = sjScenes(100, 150)
moving_scene.add(sj_scene)

# scenes fcfs

fcfs = fcfsScenes(0, 100)
moving_scene1.add(fcfs)

# scenes priority

priority = priorityScenes(0, 100)
moving_scene2.add(priority)

while True:
    game_state.state_manager()
    clock.tick(60)
