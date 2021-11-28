import pygame, sys


class pointer(pygame.sprite.Sprite):
    def __init__(self,pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.chalktap=pygame.mixer.Sound("assets/tap.mp3")
    def update(self,):
        self.rect.center=pygame.mouse.get_pos()
    def tap(self):
        self.chalktap.play()
class Interact(pygame.sprite.Sprite):
    def __init__(self,x,y,pic1,pic2):
        super().__init__() 
        self.original_image = pygame.image.load(pic1)
        self.click_image = pygame.image.load(pic2)
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.clicked = False

    def update(self,x,y):
        self.clicked = not self.clicked
        self.image = self.click_image if self.clicked else self.original_image
        self.rect = self.image.get_rect(center = (x, y))
                    
class option(pygame.sprite.Sprite):
    def __init__(self,x,y,pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect(center = (x, y))

class Scenes(pygame.sprite.Sprite):
            def __init__(self, pos_x,pos_y,scenelist,speed):
                super().__init__()
                self.sprites=scenelist
                self.is_animating = False
                self.current_sprite = 0
                self.image = self.sprites[self.current_sprite]
                self.rect = self.image.get_rect()
                self.rect.topleft = [pos_x, pos_y]
                self.speed=speed
                
            def animate(self):
                self.is_animating = not self.is_animating
            
            def update(self):
                if self.is_animating == True:
                    self.current_sprite += self.speed
                    if self.current_sprite >= len(self.sprites):
                        self.current_sprite = 0
                        self.is_animating = False
                    self.image = self.sprites[int(self.current_sprite)]
            
class GameState():
    def __init__(self):
        self.state="intro"
    def intro(self):
        event_list = pygame.event.get()
        for event in event_list:
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[proc,fc,sj,pr,st,comp,chip]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0:
                    if clicked_opts[0]==proc:
                        self.state="process_schedule"
                    elif clicked_opts[0]==fc:
                        self.state="firstcome"
                    elif clicked_opts[0]==sj:
                        self.state="shortest_job"
                    elif clicked_opts[0]==pr:
                        self.state="priority"
                    elif clicked_opts[0]==st:
                        self.state="shortest_time"
                    elif clicked_opts[0]==comp:
                        comp.update(850,475)
                    elif clicked_opts[0]==chip:
                        chip.update(400,475)
            
        screen.blit(bg,(0,0))
        #screen.blit(stage_select,(280,30))
        #screen.blit(select_num,(230,315))
        option_group.draw(screen)
        interact_group.draw(screen)
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def process_info(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0:
                    if clicked_opts[0]==barrow:
                        self.state="intro"
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(process_text,(400,40))
        screen.blit(process_desc,(200,100))
        arrow_group.draw(screen)
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def first_come_desc(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow,film]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0:
                    if clicked_opts[0]==barrow:
                        self.state="intro"
                    if clicked_opts[0]==film:
                        self.state="fc_ani"
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(firstcome_text,(400,40))
        screen.blit(fc_desc,(200,100))
        nav_group.draw(screen)
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def first_come_ani(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow,start,reset]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0: 
                    if clicked_opts[0]==barrow:
                        fc_scene.is_animating=False
                        self.state="firstcome"
                    elif clicked_opts[0]==start:
                        start.update(1100,100)
                        fc_scene.animate()
                    elif clicked_opts[0]==reset:
                        fc_scene.current_sprite = 0
                        fc_scene.image = fc_scene.sprites[sj_scene.current_sprite]
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="firstcome"
                if event.key==pygame.K_KP5:
                    fc_scene.animate()
        screen.blit(bg,(0,0))
        arrow_group.draw(screen)
        start_group.draw(screen)
        screen.blit(firstcome_text,(400,40))
        fc_group.draw(screen)
        fc_group.update()
        if sj_scene.is_animating==False:
            start.image=start.original_image
        else:
            start.image=start.click_image
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    
    def shortest_job_desc(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow,film]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0:
                    if clicked_opts[0]==barrow:
                        self.state="intro"
                    if clicked_opts[0]==film:
                        self.state="sj_ani"
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(shortest_job_text,(400,40))
        screen.blit(sj_desc,(200,100))
        nav_group.draw(screen)
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()


    def shortest_job_ani(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow,start,reset]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0: 
                    if clicked_opts[0]==barrow:
                        sj_scene.is_animating=False
                        self.state="shortest_job"
                    elif clicked_opts[0]==start:
                        start.update(1100,100)
                        sj_scene.animate()
                    elif clicked_opts[0]==reset:
                        sj_scene.current_sprite = 0
                        sj_scene.image = sj_scene.sprites[sj_scene.current_sprite]
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="shortest_job"
                if event.key==pygame.K_KP5:
                    sj_scene.animate()
        screen.blit(bg,(0,0))
        arrow_group.draw(screen)
        start_group.draw(screen)
        screen.blit(shortest_job_text,(400,40))
        sj_group.draw(screen)
        sj_group.update()
        if sj_scene.is_animating==False:
            start.image=start.original_image
        else:
            start.image=start.click_image
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def priority_desc(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow,film]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0:
                    if clicked_opts[0]==barrow:
                        self.state="intro"
                    if clicked_opts[0]==film:
                        self.state="pr_ani"
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(priority_text,(400,40))
        screen.blit(pr_desc,(200,100))
        nav_group.draw(screen)
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def priority_ani(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow,start,reset]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0: 
                    if clicked_opts[0]==barrow:
                        sj_scene.is_animating=False
                        self.state="priority"
                    elif clicked_opts[0]==start:
                        start.update(1100,100)
                        sj_scene.animate()
                    elif clicked_opts[0]==reset:
                        sj_scene.current_sprite = 0
                        sj_scene.image = sj_scene.sprites[sj_scene.current_sprite]
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="priority"
                if event.key==pygame.K_KP5:
                    sj_scene.animate()
        screen.blit(bg,(0,0))
        arrow_group.draw(screen)
        start_group.draw(screen)
        screen.blit(priority_text,(400,40))
        sj_group.draw(screen)
        sj_group.update()
        if sj_scene.is_animating==False:
            start.image=start.original_image
        else:
            start.image=start.click_image
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def shortest_time_desc(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow,film]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0:
                    if clicked_opts[0]==barrow:
                        self.state="intro"
                    if clicked_opts[0]==film:
                        self.state="st_ani"
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="intro"
        
        screen.blit(bg,(0,0))
        screen.blit(shortest_time_text,(400,40))
        screen.blit(st_desc,(200,100))
        nav_group.draw(screen)
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()
    
    def shortest_time_ani(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer.tap()
                pos = pygame.mouse.get_pos()
                optlist=[barrow,start,reset]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts)>0: 
                    if clicked_opts[0]==barrow:
                        sj_scene.is_animating=False
                        self.state="shortest_time"
                    elif clicked_opts[0]==start:
                        start.update(1100,100)
                        sj_scene.animate()
                    elif clicked_opts[0]==reset:
                        sj_scene.current_sprite = 0
                        sj_scene.image = sj_scene.sprites[sj_scene.current_sprite]
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="shortest_time"
                if event.key==pygame.K_KP5:
                    sj_scene.animate()
        screen.blit(bg,(0,0))
        arrow_group.draw(screen)
        start_group.draw(screen)
        screen.blit(shortest_time_text,(400,40))
        sj_group.draw(screen)
        sj_group.update()
        if sj_scene.is_animating==False:
            start.image=start.original_image
        else:
            start.image=start.click_image
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def state_manager(self):
        if self.state=='intro':
            self.intro()
        if self.state=='process_schedule':
            self.process_info()
        if self.state=='firstcome':
            self.first_come_desc()
        if self.state=='fc_ani':
            self.first_come_ani()
        if self.state=='shortest_job':
            self.shortest_job_desc()
        if self.state=='sj_ani':
            self.shortest_job_ani()
        if self.state=='priority':
            self.priority_desc()
        if self.state=='pr_ani':
            self.priority_ani()
        if self.state=='shortest_time':
            self.shortest_time_desc()
        if self.state=='st_ani':
            self.shortest_time_ani()

# General setup
pygame.init()
clock = pygame.time.Clock()
game_state=GameState()
# Game Screen
screen_width =1200
screen_height =700 
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load("assets/woodboard.jpg")
#comp = pygame.image.load("comp.png")
#chip = pygame.image.load("chip.png")


#Game options
stage_select=pygame.image.load('stages-images/Anim-01.png')
process_text=pygame.image.load("stages-images/Anim-00.png")
firstcome_text=pygame.image.load("stages-images/Anim-02.png")
shortest_job_text=pygame.image.load("stages-images\Anim-03.png")
priority_text=pygame.image.load("stages-images\Anim-04.png")
shortest_time_text=pygame.image.load("stages-images\Anim-05.png")
select_num=pygame.image.load('stages-images/Anim-06.png')
pygame.mouse.set_visible(False)

#Pointer
pointer = pointer("assets/pointer.png")
pointer_group = pygame.sprite.Group()
pointer_group.add(pointer)

#Navigation
barrow=option(110,40,"assets/arrow.png")
film=option(600,585,"assets/filmc.png")
arrow_group=pygame.sprite.Group([barrow])
nav_group=pygame.sprite.Group([barrow,film])

#Stage TEXT
process_desc=pygame.image.load('assets/process_desc.png')
fc_desc=pygame.image.load('assets/fc_desc.png')
sj_desc=pygame.image.load('assets/sj_desc.png')
pr_desc=pygame.image.load('assets/pr_desc.png')
st_desc=pygame.image.load('assets/st_desc.png')

""" Stage options """
#stage select options
proc=option(600,100,"stages-images/Anim-00u.png")
fc=option(280,200,"stages-images/Anim-02.png")
sj=option(280,300,"stages-images/Anim-03.png")
pr=option(850,200,"stages-images/Anim-04.png")
st=option(850,300,"stages-images/Anim-05.png")
option_group=pygame.sprite.Group([proc,fc,sj,pr,st])
comp=Interact(850,475,"assets/comp.png","assets/comp_on.png")
chip=Interact(400,475,"assets/chip.png","assets/chip_on.png")
interact_group=pygame.sprite.Group([comp,chip])

#In-Stage options
reset=option(1000,100,"assets/reset.png")
start=Interact(1100,100,"assets/Start_circle.png","assets/Stop_circle.png")
start_group=pygame.sprite.Group([start,reset])

#FCFS SCENES
fc_sprites = []
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-01.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-02.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-03.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-04.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-05.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-06.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-07.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-08.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-09.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-10.jpg"))
fc_sprites.append(pygame.image.load("fcfsimages\FCFS-11.jpg"))
fc_group = pygame.sprite.Group()        
fc_scene = Scenes(100,150,fc_sprites,0.05)
fc_group.add(fc_scene)

#scenes shortest jobs
sj_sprites = []
sj_sprites.append(pygame.image.load("SJN\Frame1.png"))
sj_sprites.append(pygame.image.load("SJN\Frame2.png"))
sj_sprites.append(pygame.image.load("SJN\Frame3.png"))
sj_sprites.append(pygame.image.load("SJN\Frame4.png"))
sj_sprites.append(pygame.image.load("SJN\Frame5.png"))
sj_sprites.append(pygame.image.load("SJN\Frame6.png"))
sj_sprites.append(pygame.image.load("SJN\Frame7.png"))
sj_sprites.append(pygame.image.load("SJN\Frame8.png"))
sj_sprites.append(pygame.image.load("SJN\Frame9.png"))
sj_sprites.append(pygame.image.load("SJN\Frame10.png"))
sj_sprites.append(pygame.image.load("SJN\Frame11.png"))
sj_sprites.append(pygame.image.load("SJN\Frame12.png"))
sj_sprites.append(pygame.image.load("SJN\Frame13.png"))
sj_sprites.append(pygame.image.load("SJN\Frame14.png"))
sj_sprites.append(pygame.image.load("SJN\Frame15.png"))
sj_sprites.append(pygame.image.load("SJN\Frame16.png"))
sj_sprites.append(pygame.image.load("SJN\Frame17.png"))
sj_sprites.append(pygame.image.load("SJN\Frame18.png"))
sj_sprites.append(pygame.image.load("SJN\Frame19.png"))
sj_sprites.append(pygame.image.load("SJN\Frame20.png"))
sj_sprites.append(pygame.image.load("SJN\Frame21.png"))
sj_sprites.append(pygame.image.load("SJN\Frame22.png"))
sj_sprites.append(pygame.image.load("SJN\Frame23.png"))
sj_sprites.append(pygame.image.load("SJN\Frame24.png"))
sj_sprites.append(pygame.image.load("SJN\Frame25.png"))
sj_sprites.append(pygame.image.load("SJN\Frame26.png"))
sj_group = pygame.sprite.Group()        
sj_scene = Scenes(100,100,sj_sprites,0.0225)
sj_group.add(sj_scene)
while True:
    game_state.state_manager()
    clock.tick(60)
