import pygame, sys
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

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

# BODY
ellipse(screen, (200, 113, 55), (50, 420, 420, 200))
ellipse(screen, (78, 45, 21), (49, 419, 422, 202), 1)

# HEAD
ellipse(screen, (200, 113, 55), (15, 430, 145, 145))
ellipse(screen, (78, 45, 21), (14, 429, 147, 147), 1)
# right ear
polygon(screen, (200, 113, 55), [(10, 430), (25, 475), (50, 450)])
polygon(screen, (78, 45, 21), [(10, 430), (25, 475), (50, 450)], 1)
polygon(screen, (222, 170, 135), [(15, 436), (27, 468), (44, 450)])
polygon(screen, (78, 45, 21), [(15, 436), (27, 468), (44, 450)], 1)
# left ear
polygon(screen, (200, 113, 55), [(145, 420), (110, 446), (140, 470)])
polygon(screen, (78, 45, 21), [(145, 420), (110, 446), (140, 470)], 1)
polygon(screen, (222, 170, 135), [(141, 427), (115, 446), (136, 462)])
polygon(screen, (78, 45, 21), [(141, 427), (115, 446), (136, 462)], 1)
# right eye
ellipse(screen, (136, 170, 0), (41, 485, 35, 43))
ellipse(screen, (78, 45, 21), (40, 484, 37, 45), 1)
# right pupil
ellipse(screen, (0, 0, 0), (60, 488, 6, 36))
# left eye
ellipse(screen, (136, 170, 0), (101, 485, 35, 43))
ellipse(screen, (78, 45, 21), (100, 484, 37, 45), 1)
# left pupil
ellipse(screen, (0, 0, 0), (120, 488, 6, 36))
# nose
polygon(screen, (222, 170, 135), [(87, 537), (80, 530), (94, 530)])
polygon(screen, (78, 45, 21), [(87, 537), (80, 530), (94, 530)], 1)
# mouth
pi = 3.14
polygon(screen, (78, 45, 21), [(87, 536), (87, 548), ], 1)
pygame.draw.arc(screen, (78, 45, 21), (82, 494, 30, 60), 4, pi/-3)
pygame.draw.arc(screen, (78, 45, 21), (65, 492, 30, 60), 4, pi/-3)
# right mustache
pi = 3.14
pygame.draw.arc(screen, (78, 45, 21), (103, 526, 100, 80), 7, (4*pi)/5)
pygame.draw.arc(screen, (78, 45, 21), (103, 532, 100, 80), 7, (4*pi)/5)
pygame.draw.arc(screen, (78, 45, 21), (103, 538, 100, 80), 7, (4*pi)/5)
# left mustache
arc(screen, (78, 45, 21), (-27, 526, 100, 80), 7, (4*pi)/5)
arc(screen, (78, 45, 21), (-27, 532, 100, 80), 7, (4*pi)/5)
arc(screen, (78, 45, 21), (-27, 538, 100, 80), 7, (4*pi)/5)

# PAWS
# right paw
ellipse(screen, (200, 113, 55), (36, 500, 48, 88))
ellipse(screen, (78, 45, 21), (35, 499, 50, 90), 1)
# left paw
ellipse(screen, (200, 113, 55), (81, 574, 98, 53))
ellipse(screen, (78, 45, 21), (80, 574, 100, 55), 1)
# hind paw
circle(screen, (200, 113, 55), (410, 570), 65)
circle(screen, (78, 45, 21), (410, 570), 65, 1)
ellipse(screen, (200, 113, 55), (451, 586, 37, 92))
ellipse(screen, (78, 45, 21), (450, 585, 39, 94), 1)

# clew
circle(screen, (153, 153, 153), (350, 730), 60)
circle(screen, (78, 45, 21), (350, 730), 60, 1)
# lines on the clew


# lines near the clew



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
