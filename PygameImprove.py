import pygame,sys
from pygame.locals import*

def hand():
    for event in pygame.event.get():#event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex,mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex,mousey = event.pos
            mouseClicked = True
