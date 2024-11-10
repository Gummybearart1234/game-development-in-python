import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Whack-a-Mole")
height=900
width=900
pipe_gap=200
platforms=[]
pipes=[]
pipe_speed=(4.97)
bg = pygame.image.load("4622710.png")
bg = pygame.transform.scale(bg, (900, 900))
birb= pygame.image.load("325-3257134_flappy-bird-flappy-bird-sprite-png.png")
birb = pygame.transform.scale(birb, (100, 100))
pipe= pygame.image.load("181-1811759_flappy-bird-pipes-png-transparent-download-8-bit.webp")
start=pygame.image.load("Start-button-sprite.png")
platform1=pygame.image.load("R-removebg-preveiw.png")
screen.blit(bg,(0,0) )
gravity=0.025
jump=-1
bird_show=False
button_show=True
platform_speed=2
pipe_width=100
pipe_height=200
score1=0
score_font=pygame.font.Font("ariel",20)
def create_platform():
    y=height-platform1.get_height()
    return platform1.get_rect(midbottom=(width,y))
    
def create_pipes():
    pipe_height=random.randint(50,height-pipe_gap-50)
    bottom_pipe_rect=pygame.Rect(width,0,pipe_width,pipe_height)
    top_pipe_rect=pygame.Rect(width,0,pipe_width,pipe_height)
    return top_pipe_rect, bottom_pipe_rect

platforms=[create_platform()for i in range(2)]
pipes=[create_pipes()for i in range(2)]
def display_score():

def collision():

def draw_platform():
    for platform in platforms:
       platform.x-=platform_speed
       screen.blit(platform1,platform)
    if platforms[-1].right<width:
        platforms.append(create_platform())
    if platforms[-1].right<0:
        platforms.pop(0)

def draw_pipes():
    global score1
    for top_pipe, bottom_pipe:
    top_pipe.x-=pipe_speed:
    screen.blit(pipe), top_pipe
    screen.blit(pipe, bottom_pipe)
     def check collision 




























    
