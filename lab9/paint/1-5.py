import pygame, sys
import math
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

pygame.init()
sc = pygame.display.set_mode((800, 600))
check = True
check_draw = False
color = "white"
start_pos = (0, 0)
end_pps = (0, 0)

rect_flag = False
circle_flag = False
eq_triangle_flag = False
square_flag = False
equal_triangle = False
romb_flag = False
width_line = 2

eraser = pygame.image.load("eraser.png")
eraser = pygame.transform.scale(eraser, (75, 75))

pygame.display.set_caption('TiSoft paint')

while check:
    sc.blit(eraser, (350, 510))
    pygame.draw.rect(sc, (255, 255, 255), (480, 520, 60, 60))
    pygame.draw.circle(sc, (255, 255, 255), (620, 550), 35)
    pygame.draw.circle(sc, 'red', (50, 550), 25)
    pygame.draw.circle(sc, 'blue', (125, 550), 25)
    pygame.draw.circle(sc, 'green', (200, 550), 25)
    pygame.draw.circle(sc, 'white', (275, 550), 25)
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
        if (rect_flag or circle_flag or square_flag or romb_flag or eq_triangle_flag or equal_triangle) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
            check_draw = True


        if event.type == pygame.MOUSEMOTION:
            if check_draw:
                end_pos = event.pos
                pygame.draw.line(sc, color, start_pos, end_pos, width_line)
                start_pos = end_pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            check_draw = False
            
            if square_flag:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = width_rect
                pygame.draw.rect(sc, color, pygame.Rect(x, y, width_rect, height_rect))
            elif rect_flag:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = max(end_pos[1], start_pos[1]) - y
                pygame.draw.rect(sc, color, pygame.Rect(x, y, width_rect, height_rect))
            elif circle_flag:
                end_pos = event.pos
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]
                radius = int(math.sqrt(dx ** 2 + dy ** 2)/2)
                cent = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(sc, color, cent, radius)
            elif eq_triangle_flag:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = max(end_pos[1], start_pos[1]) - y
                pygame.draw.polygon(sc, color, [(x+width_rect, y), (x, y), (x+width_rect, y+height_rect)])
            elif equal_triangle:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = max(end_pos[1], start_pos[1]) - y
                pygame.draw.polygon(sc, color, [(x,y), (x+width_rect, y), (x+width_rect/2, y-width_rect*math.sqrt(3)//2)])
            elif romb_flag:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = max(end_pos[1], start_pos[1]) - y
                pygame.draw.polygon(sc, color, [(x,y), (x+width_rect, y), (x+width_rect/2, y+width_rect*math.sqrt(3)//2)])
                pygame.draw.polygon(sc, color, [(x,y), (x+width_rect, y), (x+width_rect/2, y-width_rect*math.sqrt(3)//2)])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            # print(event.pos)
            if 25 <= event.pos[0] <= 75 and 525 <= event.pos[1] <= 575:
                square_flag=False
                romb_flag=False
                equal_triangle=False
                eq_triangle_flag = False
                rect_flag = False
                circle_flag = False
                color = 'red'
                width_line = 2
            elif 100 <= event.pos[0] <= 150 and 525 <= event.pos[1] <= 575:
                square_flag=False
                romb_flag=False
                equal_triangle=False
                eq_triangle_flag = False
                rect_flag = False
                circle_flag = False
                color = "blue"
                width_line = 2
            elif 175 <= event.pos[0] <= 225 and 525 <= event.pos[1] <= 575:
                square_flag=False
                romb_flag=False
                equal_triangle=False
                eq_triangle_flag = False
                rect_flag = False
                circle_flag = False
                width_line = 2
                color = "green"
            elif 250 <= event.pos[0] <= 300 and 525 <= event.pos[1] <= 575:
                square_flag=False
                romb_flag=False
                equal_triangle=False
                eq_triangle_flag = False
                rect_flag = False
                circle_flag = False
                color = "white"
                width_line = 2
            elif 350 <= event.pos[0] <= 425 and 510 <= event.pos[1] <= 580:
                square_flag=False
                romb_flag=False
                equal_triangle=False
                eq_triangle_flag = False
                rect_flag = False
                circle_flag = False
                color = "black"
                width_line = 40
            elif 475 <= event.pos[0] <= 540 and 515 <= event.pos[1] <= 580:
                eq_triangle_flag = False
                rect_flag = True
                check_draw = False
                circle_flag = False
                square_flag=False
                romb_flag=False
                equal_triangle=False
            elif 585 <= event.pos[0] <= 655 and 510 <= event.pos[1] <= 585:
                eq_triangle_flag = False
                rect_flag = False
                check_draw = False
                circle_flag = True
                square_flag=False
                romb_flag=False
                equal_triangle=False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                sc.fill(0)
            elif event.key == pygame.K_z:
                square_flag=True
                romb_flag=False
                equal_triangle=False
                eq_triangle_flag = False
                rect_flag = False
                check_draw = False
                circle_flag = False
            elif event.key == pygame.K_x:
                square_flag=False
                romb_flag=True
                equal_triangle=False
                eq_triangle_flag = False
                rect_flag = False
                check_draw = False
                circle_flag = False
            elif event.key == pygame.K_c:
                square_flag=False
                romb_flag=False
                equal_triangle=True
                eq_triangle_flag = False
                rect_flag = False
                check_draw = False
                circle_flag = False
            elif event.key == pygame.K_v:
                square_flag=False
                romb_flag=False
                equal_triangle=False
                eq_triangle_flag = True
                rect_flag = False
                check_draw = False
                circle_flag = False
    pygame.display.update()

pygame.quit()