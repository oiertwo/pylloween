__author__ = 'oier'



import pygame
import time

def lightning():
    white = (255,255,255)
    black = (1,1,1)
    (width, height) = (1366, 768)
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption('Tutorial 1')
    pygame.mouse.set_visible(False)
    screen.fill(black)

    screen.fill(black)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(white)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(black)
    pygame.display.update()
    time.sleep(0.5)
    screen.fill(white)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(black)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(white)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(black)
    pygame.display.update()
    time.sleep(0.1)
    screen.fill(white)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(black)
    pygame.display.update()
    time.sleep(0.1)
    screen.fill(white)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(black)
    pygame.display.update()
    time.sleep(0.3)
    screen.fill(white)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(black)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(white)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(black)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(white)
    pygame.display.update()
    time.sleep(0.2)
    screen.fill(black)
    pygame.display.update()
    time.sleep(0.2)
    pygame.quit()


lightning()
