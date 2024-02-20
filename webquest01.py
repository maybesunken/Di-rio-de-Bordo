# -*- coding: latin-1 -*-
energia0 = 'desenho00.jpg'
energia1 = 'desenho01.jpg'
energia2 = 'desenho02.jpg'
energia3 = 'desenho03.jpg'
energia4 = 'desenho04.jpg'
energia5 = 'desenho05.jpg'
energia6 = 'desenho06.jpg'
energia7 = 'desenho07.jpg'
energia8 = 'desenho08.jpg'
energia9 =  'desenho09.jpg'
energia10 = 'desenho10.jpg'

estado = 0

import pygame, sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((650,900),0,0)

tela0=pygame.image.load(energia0).convert()
tela1=pygame.image.load(energia1).convert()
tela2=pygame.image.load(energia2).convert()
tela3=pygame.image.load(energia3).convert()
tela4=pygame.image.load(energia4).convert()
tela5=pygame.image.load(energia5).convert()
tela6=pygame.image.load(energia6).convert()
tela7=pygame.image.load(energia7).convert()
tela8=pygame.image.load(energia8).convert()
tela9=pygame.image.load(energia9).convert()
tela10=pygame.image.load(energia10).convert()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if (event.type == MOUSEBUTTONUP) and (estado == 0):
            screen.blit(tela0, (0,0))
            estado = 1

        elif (event.type == MOUSEBUTTONUP) and (estado == 1):
            screen.blit(tela1, (0,0))
            estado = 2

        elif (event.type == MOUSEBUTTONUP) and (estado == 2):
            screen.blit(tela2, (0,0))
            estado = 3

        elif (event.type == MOUSEBUTTONUP) and (estado == 3):
            screen.blit(tela3, (0,0))
            estado = 4

        elif (event.type == MOUSEBUTTONUP) and (estado == 4):
            screen.blit(tela4, (0,0))
            estado = 5

        elif (event.type == MOUSEBUTTONUP) and (estado == 5):
            screen.blit(tela5, (0,0))
            estado = 6

        elif (event.type == MOUSEBUTTONUP) and (estado == 6):
            screen.blit(tela6, (0,0))
            estado = 7

        elif (event.type == MOUSEBUTTONUP) and (estado == 7):
            screen.blit(tela7, (0,0))
            estado = 8

        elif (event.type == MOUSEBUTTONUP) and (estado == 8):
            screen.blit(tela8, (0,0))
            estado = 9 

        elif (event.type == MOUSEBUTTONUP) and (estado == 9):
            screen.blit(tela9, (0,0))
            estado = 10  

        elif (event.type == MOUSEBUTTONUP) and (estado == 10):
            screen.blit(tela10, (0,0))
            estado = 11
    pygame.display.update()