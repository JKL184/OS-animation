import pygame
import sys
import numpy as np
import time
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
    def __init__(self, x, y, pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect(center=(x, y))


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
                optlist = [barrow]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                if len(clicked_opts) > 0:
                    if clicked_opts[0] == barrow:
                        self.state = "intro"
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
                optlist=[barrow,start,reset,film]
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
                        fc_scene.image = fc_scene.sprites[fc_scene.current_sprite]
                    elif clicked_opts[0]==film:
                        self.state="fc_test"
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="firstcome"
                if event.key==pygame.K_KP5:
                    fc_scene.animate()
        screen.blit(bg,(0,0))
        arrow_group.draw(screen)
        nav_group.draw(screen)
        start_group.draw(screen)
        screen.blit(firstcome_text,(400,40))
        fc_group.draw(screen)
        fc_group.update()
        if fc_scene.is_animating==False:
            start.image=start.original_image
        else:
            start.image=start.click_image
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    
    def first_come_test(self):
        global arr1_st,arr2_st,arr3_st,br1_st,br2_st,br3_st,Proc1,Proc2,Proc3,Arr,Exc,P1,P2,P3,b1,b2,b3,b0
        event_list = pygame.event.get()
        pos = pygame.mouse.get_pos()
        
        global arr1_text,arr2_text,arr3_text,br1_text,br2_text,br3_text
        numkeys=[pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,
        pygame.K_KP0,pygame.K_KP1,pygame.K_KP2,pygame.K_KP3,pygame.K_KP4,pygame.K_KP5,pygame.K_KP6,pygame.K_KP7,
        pygame.K_KP8,pygame.K_KP9]
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                arr1_st,arr2_st,arr3_st,br1_st,br2_st,br3_st=False,False,False,False,False,False
                pointer.tap()
                optlist=[barrow,start,reset]
                inlist=[arr1_rect,arr2_rect,arr3_rect,br1_rect,br2_rect,br3_rect]
                clicked_opts = [s for s in optlist if s.rect.collidepoint(pos)]
                input_opts = [s for s in inlist if s.collidepoint(pos)]
                if len(clicked_opts)>0: 
                    if clicked_opts[0]==barrow:
                        self.state="fc_ani"
                    elif clicked_opts[0]==start:
                        bar1_rect.w,bar1_rect.h,bar2_rect.w,bar2_rect.h,bar3_rect.w,bar3_rect.h=0,0,0,0,0,0
                        arr1=int(arr1_text)
                        arr2=int(arr2_text)
                        arr3=int(arr3_text)
                        ardict={"Pr1":arr1,"Pr2":arr2,"Pr3":arr3}
                        a_order=[k for k, v in sorted(ardict.items(), key=lambda item: item[1])]
                        br1=int(br1_text)
                        br2=int(br2_text)
                        br3=int(br3_text)
                        brdict={"Pr1":br1,"Pr2":br2,"Pr3":br3}
                        brecdict={"Pr1":bar1_rect,"Pr2":bar2_rect,"Pr3":bar3_rect}
                        bar1_rect.x,bar2_rect.x,bar3_rect.x=100,100,100
                        bar1_rect.h,bar2_rect.h,bar3_rect.h=75,75,75
                        cm=np.cumsum([brdict[a_order[0]],brdict[a_order[1]],brdict[a_order[2]]])
                        for b in range(len(a_order)):
                            if a_order[b]=="Pr1":
                                b1=str(cm[b])
                            elif a_order[b]=="Pr2":
                                b2=str(cm[b])
                            elif a_order[b]=="Pr3":
                                b3=str(cm[b])
                        for a in range(len(a_order)):
                            if a_order[a] !=a_order[0]:
                                brecdict[a_order[a]].x=(brecdict[a_order[a-1]].topright)[0]+2
                            for i in range(brdict[a_order[a]]):
                                brecdict[a_order[a]].w+=20
                        P1,P2,P3,b0="P1","P2","P3","0"
                        
                    elif clicked_opts[0]==reset:
                        bar1_rect.w,bar1_rect.h,bar2_rect.w,bar2_rect.h,bar3_rect.w,bar3_rect.h=0,0,0,0,0,0
                        P1,P2,P3,b1,b2,b3,b0="","","","","","",""
                        
                if len(input_opts)>0:
                    if input_opts[0]==arr1_rect:
                        arr1_st=True
                    if input_opts[0]==arr2_rect:
                        arr2_st=True
                    if input_opts[0]==arr3_rect:
                        arr3_st=True
                    if input_opts[0]==br1_rect:
                        br1_st=True
                    if input_opts[0]==br2_rect:
                        br2_st=True
                    if input_opts[0]==br3_rect:
                        br3_st=True   
            if event.type == pygame.KEYDOWN:
                if arr1_st:
                        if event.key == pygame.K_BACKSPACE:
                            arr1_text=arr1_text[:-1]
                        elif event.key in numkeys :
                            if len(arr1_text)<6:
                                arr1_text+=event.unicode
                if arr2_st:
                        if event.key == pygame.K_BACKSPACE:
                            arr2_text=arr2_text[:-1]
                        elif event.key in numkeys :
                            if len(arr2_text)<6:
                                arr2_text+=event.unicode
                if arr3_st:
                        if event.key == pygame.K_BACKSPACE:
                            arr3_text=arr3_text[:-1]
                        elif event.key in numkeys :
                            if len(arr3_text)<6:
                                arr3_text+=event.unicode
                if br1_st:
                        if event.key == pygame.K_BACKSPACE:
                            br1_text=br1_text[:-1]
                        elif event.key in numkeys :
                            if len(br1_text)<6:
                                br1_text+=event.unicode
                if br2_st:
                        if event.key == pygame.K_BACKSPACE:
                            br2_text=br2_text[:-1]
                        elif event.key in numkeys :
                            if len(br2_text)<6:
                                br2_text+=event.unicode
                if br3_st:
                        if event.key == pygame.K_BACKSPACE:
                            br3_text=br3_text[:-1]
                        elif event.key in numkeys :
                            if len(br3_text)<6:
                                br3_text+=event.unicode
                
        screen.blit(bg,(0,0))
        arrow_group.draw(screen)
        start_group.draw(screen)
        
        pygame.draw.rect(screen, "green",bar1_rect,0)
        bar1_surface=base_font.render(P1, True, (0,0,0))
        screen.blit(bar1_surface,(bar1_rect.x+5,bar1_rect.y+5))
        bar0_exc=base_font.render(b0, True, (255,255,255))
        screen.blit(bar0_exc,(100,575))
        bar1_exc=base_font.render(b1, True, (255,255,255))
        screen.blit(bar1_exc,(bar1_rect.bottomright))
        pygame.draw.rect(screen, "red",bar2_rect,0)
        bar2_surface=base_font.render(P2, True, (0,0,0))
        screen.blit(bar2_surface,(bar2_rect.x+5,bar2_rect.y+5))
        bar2_exc=base_font.render(b2, True, (255,255,255))
        screen.blit(bar2_exc,(bar2_rect.bottomright))
        pygame.draw.rect(screen, "yellow",bar3_rect,0)
        bar3_surface=base_font.render(P3, True, (0,0,0))
        screen.blit(bar3_surface,(bar3_rect.x+5,bar3_rect.y+5))
        bar3_exc=base_font.render(b3, True, (255,255,255))
        screen.blit(bar3_exc,(bar3_rect.bottomright))
        screen.blit(firstcome_text,(400,40))
        arr1_title=base_font.render(Proc1,True,(255,255,255))
        arr2_title=base_font.render(Proc2,True,(255,255,255))
        arr3_title=base_font.render(Proc3,True,(255,255,255))
        arr_title=base_font.render(Arr,True,(255,255,255))
        exc_title=base_font.render(Exc,True,(255,255,255))
        screen.blit(arr1_title,(800,300))
        screen.blit(arr2_title,(800,400))
        screen.blit(arr3_title,(800,500))
        screen.blit(arr_title,(900,270))
        screen.blit(exc_title,(1000,270))
        if arr1_st:
            pygame.draw.rect(screen, color_active,arr1_rect, 2)
        else:
            pygame.draw.rect(screen, color_passive,arr1_rect, 2)
        if arr2_st:
            pygame.draw.rect(screen, color_active,arr2_rect, 2)
        else:
            pygame.draw.rect(screen, color_passive,arr2_rect, 2)
        if arr3_st:
            pygame.draw.rect(screen, color_active,arr3_rect, 2)
        else:
            pygame.draw.rect(screen, color_passive,arr3_rect, 2)
        if br1_st:
            pygame.draw.rect(screen, color_active,br1_rect,2)
        else:
            pygame.draw.rect(screen, color_passive,br1_rect,2)
        if br2_st:
            pygame.draw.rect(screen, color_active,br2_rect,2)
        else:
            pygame.draw.rect(screen, color_passive,br2_rect,2)
        if br3_st:
            pygame.draw.rect(screen, color_active,br3_rect,2)
        else:
            pygame.draw.rect(screen, color_passive,br3_rect,2)
        arr1_surface=base_font.render(arr1_text, True, (255,255,255))
        screen.blit(arr1_surface,(arr1_rect.x+5,arr1_rect.y+5))
        arr2_surface=base_font.render(arr2_text, True, (255,255,255))
        screen.blit(arr2_surface,(arr2_rect.x+5,arr2_rect.y+5))
        arr3_surface=base_font.render(arr3_text, True, (255,255,255))
        screen.blit(arr3_surface,(arr3_rect.x+5,arr3_rect.y+5))
        br1_surface=base_font.render(br1_text, True, (255,255,255))
        screen.blit(br1_surface,(br1_rect.x+5,br1_rect.y+5))
        br2_surface=base_font.render(br2_text, True, (255,255,255))
        screen.blit(br2_surface,(br2_rect.x+5,br2_rect.y+5))
        br3_surface=base_font.render(br3_text, True, (255,255,255))
        screen.blit(br3_surface,(br3_rect.x+5,br3_rect.y+5))
        
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
                        pr_scene.is_animating=False
                        self.state="priority"
                    elif clicked_opts[0]==start:
                        start.update(1100,100)
                        pr_scene.animate()
                    elif clicked_opts[0]==reset:
                        pr_scene.current_sprite = 0
                        pr_scene.image = pr_scene.sprites[pr_scene.current_sprite]
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="priority"
                if event.key==pygame.K_KP5:
                    pr_scene.animate()
        screen.blit(bg,(0,0))
        arrow_group.draw(screen)
        start_group.draw(screen)
        screen.blit(priority_text,(400,40))
        pr_group.draw(screen)
        pr_group.update()
        if pr_scene.is_animating==False:
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
                        str_scene.is_animating=False
                        self.state="shortest_time"
                    elif clicked_opts[0]==start:
                        start.update(1100,100)
                        str_scene.animate()
                    elif clicked_opts[0]==reset:
                        str_scene.current_sprite = 0
                        str_scene.image = str_scene.sprites[str_scene.current_sprite]
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_KP0:
                    self.state="shortest_time"
                if event.key==pygame.K_KP5:
                    str_scene.animate()
        screen.blit(bg,(0,0))
        arrow_group.draw(screen)
        start_group.draw(screen)
        screen.blit(shortest_time_text,(400,40))
        str_group.draw(screen)
        str_group.update()
        if str_scene.is_animating==False:
            start.image=start.original_image
        else:
            start.image=start.click_image
        pointer_group.draw(screen)
        pointer_group.update()
        pygame.display.flip()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state=='process_schedule':
            self.process_info()
        if self.state=='firstcome':
            self.first_come_desc()
        if self.state=='fc_ani':
            self.first_come_ani()
        if self.state=='fc_test':
            self.first_come_test()
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
game_state = GameState()
# Game Screen

screen_width =1200
screen_height =700 
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load("assets/woodboard.jpg")
base_font=pygame.font.Font(None,28)



Proc1="Process 1"
Proc2="Process 2"
Proc3="Process 3"
P1,P2,P3,b0,b1,b2,b3="","","","","","",""
Arr="Arrival"
Exc="Execution"

arr1_text, arr2_text, arr3_text , br1_text, br2_text, br3_text ="0","0","0","0","0","0"
arr1_rect=pygame.Rect(900, 300, 75,32)
arr2_rect=pygame.Rect(900, 400, 75,32)
arr3_rect=pygame.Rect(900, 500, 75,32)
br1_rect=pygame.Rect(1000, 300, 75,32)
br2_rect=pygame.Rect(1000, 400, 75,32)
br3_rect=pygame.Rect(1000, 500, 75,32)
bar1_rect=pygame.Rect(100, 500,0,0)
bar2_rect=pygame.Rect(100, 500,0,0)
bar3_rect=pygame.Rect(100, 500,0,0)
color_active=pygame.Color('lightskyblue3')
color_passive = pygame.Color('red2')
color = color_passive
arr1_st,arr2_st,arr3_st,br1_st,br2_st,br3_st=False,False,False,False,False,False
#Game options
stage_select=pygame.image.load('stages-images/Anim-01.png')
process_text=pygame.image.load("stages-images/Anim-00.png")
firstcome_text=pygame.image.load("stages-images/Anim-02.png")
shortest_job_text=pygame.image.load("stages-images\Anim-03.png")
priority_text=pygame.image.load("stages-images\Anim-04.png")
shortest_time_text=pygame.image.load("stages-images\Anim-05.png")
select_num=pygame.image.load('stages-images/Anim-06.png')
pygame.mouse.set_visible(False)

# Pointer
pointer = pointer("assets/pointer.png")
pointer_group = pygame.sprite.Group()
pointer_group.add(pointer)

#Navigation
barrow=option(110,55,"assets/arrow.png")
film=option(600,585,"assets/filmc.png")
arrow_group=pygame.sprite.Group([barrow])
nav_group=pygame.sprite.Group([barrow,film])

#Stage TEXT
process_desc=pygame.image.load('assets/process_desc.png')
fc_desc=pygame.image.load('assets/fc_desc.png')
sj_desc=pygame.image.load('assets/sj_desc.png')
pr_desc=pygame.image.load('assets/pr_Desc.png')
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
fc_scene = Scenes(200,150,fc_sprites,0.01)
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
sj_scene = Scenes(300,100,sj_sprites,0.0225)
sj_group.add(sj_scene)

#shortest time remaining
str_sprites = []
str_sprites.append(pygame.image.load("STR\T=0.png"))
str_sprites.append(pygame.image.load("STR\T=1.png"))
str_sprites.append(pygame.image.load("STR\T=2.png"))
str_sprites.append(pygame.image.load("STR\T=3.png"))
str_sprites.append(pygame.image.load("STR\T=4.png"))
str_sprites.append(pygame.image.load("STR\T=5.png"))
str_sprites.append(pygame.image.load("STR\T=6.png"))
str_sprites.append(pygame.image.load("STR\T=7.png"))
str_sprites.append(pygame.image.load("STR\T=8.png"))
str_sprites.append(pygame.image.load("STR\T=9.png"))
str_sprites.append(pygame.image.load("STR\T=10.png"))
str_sprites.append(pygame.image.load("STR\T=11.png"))
str_sprites.append(pygame.image.load("STR\T=12.png"))
str_sprites.append(pygame.image.load("STR\T=13.png"))
str_sprites.append(pygame.image.load("STR\T=14.png"))
str_sprites.append(pygame.image.load("STR\T=15.png"))
str_sprites.append(pygame.image.load("STR\T=16.png"))
str_sprites.append(pygame.image.load("STR\T=17.png"))
str_sprites.append(pygame.image.load("STR\T=18.png"))
str_sprites.append(pygame.image.load("STR\T=19.png"))
str_sprites.append(pygame.image.load("STR\T=20.png"))
str_sprites.append(pygame.image.load("STR\T=21.png"))
str_sprites.append(pygame.image.load("STR\T=22.png"))
str_sprites.append(pygame.image.load("STR\T=23.png"))
str_sprites.append(pygame.image.load("STR\T=24.png"))
str_sprites.append(pygame.image.load("STR\T=25.png"))
str_sprites.append(pygame.image.load("STR\T=26.png"))
str_sprites.append(pygame.image.load("STR\T=27.png"))
str_group = pygame.sprite.Group()        
str_scene = Scenes(300,100,str_sprites,0.0225)
str_group.add(str_scene)

pr_sprites = []
pr_sprites.append(pygame.image.load(
    "priority/scene1.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-1.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-2.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-3.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-4.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-5.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-6.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-7.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-8.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-9.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-10.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-11.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-12.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-13.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-14.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-15.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-16.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-17.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-18.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-19.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-20.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-21.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-22.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-23.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-24.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-25.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-26.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-27.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-28.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-29.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-30.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-31.png"))
pr_sprites.append(pygame.image.load(
    "priority/scene1-32.png"))
pr_sprites.append(pygame.image.load("priority/scene1-33.png"))
pr_group = pygame.sprite.Group()        
pr_scene = Scenes(200,100,pr_sprites,0.0225)
pr_group.add(pr_scene)

while True:
    game_state.state_manager()
    clock.tick(60)
