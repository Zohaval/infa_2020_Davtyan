import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
N = int(input())
i = 1
pi = 3.14

# BACK GROUND
rect(screen, (128, 102, 0), (0, 400, 800, 800))
rect(screen, (85, 68, 0), (0, 0, 800, 400))

# WINDOWS FRAME
rect(screen, (213, 255, 230), (330, 20, 260, 360))
# top glass
rect(screen, (135, 205, 222), (345, 30, 108, 100))
rect(screen, (135, 205, 222), (470, 30, 108, 100))
# Below Glass
rect(screen, (135, 205, 222), (345, 150, 108, 210))
rect(screen, (135, 205, 222), (470, 150, 108, 210))

while i <= N:
    def draw_cat(x, y, k):

        # BODY
        # tail
        ellipse(screen, (200, 113, 55), (x+420//k, y+460//k, 250//k, 80//k))
        ellipse(screen, (78, 45, 21), (x+419//k, y+459//k, 252//k, 82//k), 1)
        # torso
        ellipse(screen, (200, 113, 55), (x+50//k, y+420//k, 420//k, 200//k))
        ellipse(screen, (78, 45, 21), (x+49//k, y+419//k, 422//k, 202//k), 1)
        # right paw
        ellipse(screen, (200, 113, 55), (x+36//k, y+500//k, 48//k, 88//k))
        ellipse(screen, (78, 45, 21), (x+35//k, y+499//k, 50//k, 90//k), 1)

        # HEAD
        ellipse(screen, (200, 113, 55), (x+15//k, y+430//k, 145//k, 145//k))
        ellipse(screen, (78, 45, 21), (x+14//k, y+429//k, 147//k, 147//k), 1)
        # right ear
        polygon(screen, (200, 113, 55), [(x+10//k, y+430//k), (x+25//k, y+475//k), (x+50//k, y+450//k)])
        polygon(screen, (78, 45, 21), [(x+10//k, y+430//k), (x+25//k, y+475//k), (x+50//k, y+450//k)], 1)
        polygon(screen, (222, 170, 135), [(x+15//k, y+436//k), (x+27//k, y+468//k), (x+44//k, y+450//k)])
        polygon(screen, (78, 45, 21), [(x+15//k, y+436//k), (x+27//k, y+468//k), (x+44//k, y+450//k)], 1)
        # left ear
        polygon(screen, (200, 113, 55), [(x+145//k, y+420//k), (x+110//k, y+446//k), (x+140//k, y+470//k)])
        polygon(screen, (78, 45, 21), [(x+145//k, y+420//k), (x+110//k, y+446//k), (x+140//k, y+470//k)], 1)
        polygon(screen, (222, 170, 135), [(x+141//k, y+427//k), (x+115//k, y+446//k), (x+136//k, y+462//k)])
        polygon(screen, (78, 45, 21), [(x+141//k, y+427//k), (x+115//k, y+446//k), (x+136//k, y+462//k)], 1)
        # right eye
        ellipse(screen, (136, 170, 0), (x+41//k, y+485//k, 35//k, 43//k))
        ellipse(screen, (78, 45, 21), (x+40//k, y+484//k, 37//k, 45//k), 1)
        # right pupil
        ellipse(screen, (0, 0, 0), (x+60//k, y+488//k, 6//k, 36//k))
        # left eye
        ellipse(screen, (136, 170, 0), (x+101//k, y+485//k, 35//k, 43//k))
        ellipse(screen, (78, 45, 21), (x+100//k, y+484//k, 37//k, 45//k), 1)
        # left pupil
        ellipse(screen, (0, 0, 0), (x+120//k, y+488//k, 6//k, 36//k))
        # nose
        polygon(screen, (222, 170, 135), [(x+87//k, y+537//k), (x+80//k, y+530//k), (x+94//k, y+530//k)])
        polygon(screen, (78, 45, 21), [(x+87//k, y+537//k), (x+80//k, y+530//k), (x+94//k, y+530//k)], 1)
        # mouth
        pi = 3.14
        polygon(screen, (78, 45, 21), [(x+87//k, y+536//k), (x+87//k, y+548//k), ], 1)
        pygame.draw.arc(screen, (78, 45, 21), (x+82//k, y+494//k, 30//k, 60//k), 4, pi/-3)
        pygame.draw.arc(screen, (78, 45, 21), (x+65//k, y+492//k, 30//k, 60//k), 4, pi/-3)
        # right mustache
        pi = 3.14
        pygame.draw.arc(screen, (78, 45, 21), (x+103//k, y+526//k, 100//k, 80//k), 7, (4*pi)/5)
        pygame.draw.arc(screen, (78, 45, 21), (x+103//k, y+532//k, 100//k, 80//k), 7, (4*pi)/5)
        pygame.draw.arc(screen, (78, 45, 21), (x+103//k, y+538//k, 100//k, 80//k), 7, (4*pi)/5)
        # left mustache
        arc(screen, (78, 45, 21), (x+-27//k, y+526//k, 100//k, 80//k), 7, (4*pi)/5)
        arc(screen, (78, 45, 21), (x+-27//k, y+532//k, 100//k, 80//k), 7, (4*pi)/5)
        arc(screen, (78, 45, 21), (x+-27//k, y+538//k, 100//k, 80//k), 7, (4*pi)/5)

        # PAWS
        ellipse(screen, (200, 113, 55), (x+81//k, y+574//k, 98//k, 53//k))
        ellipse(screen, (78, 45, 21), (x+80//k, y+574//k, 100//k, 55//k), 1)
        # hind paw
        circle(screen, (200, 113, 55), (x+410//k, y+570//k), 65//k)
        circle(screen, (78, 45, 21), (x+410//k, y+570//k), 65//k, 1)
        ellipse(screen, (200, 113, 55), (x+451//k, y+586//k, 37//k, 92//k))
        ellipse(screen, (78, 45, 21), (x+450//k, y+585//k, 39//k, 94//k), 1)


    draw_cat(300, 0 + (150*i), 2)
    i += 1

# clew
circle(screen, (153, 153, 153), (350, 730), 60)
circle(screen, (78, 45, 21), (350, 730), 60, 1)
# lines on the clew
arc(screen, (78, 45, 21), (305, 700, 100, 80), 2, pi)
arc(screen, (78, 45, 21), (315, 715, 100, 80), 2, pi)
arc(screen, (78, 45, 21), (325, 730, 100, 80), 2, pi)
arc(screen, (78, 45, 21), (295, 690, 100, 80), 6, pi/2)
arc(screen, (78, 45, 21), (285, 710, 100, 80), -1/3, pi/5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
