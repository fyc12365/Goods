import pygame
import time
from sys import exit
from pygame.locals import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.mixer.music.load("Data/bgm.ogg")
pygame.mixer.music.play(-1,0)
pygame.mouse.set_visible(False)
mouse_replace = pygame.image.load("Data/mouse.png")
pygame.display.set_caption("=￣w￣=")
pygame.display.set_icon(pygame.image.load("Data/icon.png"))
clock = pygame.time.Clock()
textFont_1 = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',50)
text_1 = textFont_1.render("开任务管理器是cxk!",True,(0,0,0))
cxk_1 = pygame.image.load("Data/1.jpg")
time_0 = time.time()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        pass
    screen.fill((255,255,255))
    if time.time() < time_0 + 5:
        screen.blit(text_1,(0,0))
    x,y = pygame.mouse.get_pos()
    screen.blit(mouse_replace,(x,y))
    pygame.display.update()