import pygame
import time
import random

pygame.init()


#Colores

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Tamaño de la pantalla

width = 600
height = 400

#Crear pantalla

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

#Reloj
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width/ 6, height / 3])