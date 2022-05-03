import pygame
import os
import random
audiorec = []
imgrec = []
running = True
pickedking=False
WIDTH = 400
HEIGHT = 500
FPS = 60
screen = None
clock = None
pickedred, pickedblack = None, None
pickedFlag = False
picked = None
board = [
    [["w-r", 1, (0, 100)], ["b-r", 1, (50, 100)], ["w-r", 1, (100, 100)], ["b-r", 1, (150, 100)],
     ["w-r", 1, (200, 100)], ["b-r", 1, (250, 100)], ["w-r", 1, (300, 100)], ["b-r", 1, (350, 100)]],
    [["b-r", 0, (0, 150)], ["w-r", 0, (50, 150)], ["b-r", 0, (100, 150)], ["w-r", 0, (150, 150)],
     ["b-r", 0, (200, 150)], ["w-r", 0, (250, 150)], ["b-r", 0, (300, 150)], ["w-r", 0, (350, 150)]],
    [["w-e", 0, (0, 200)], ["b-e", 0, (50, 200)], ["w-e", 0, (100, 200)], ["b-e", 0, (150, 200)],
     ["w-e", 0, (200, 200)], ["b-e", 0, (250, 200)], ["w-e", 0, (300, 200)], ["b-e", 0, (350, 200)]],
    [["b-e", 0, (0, 250)], ["w-e", 0, (50, 250)], ["b-e", 0, (100, 250)], ["w-e", 0, (150, 250)],
     ["b-e", 0, (200, 250)], ["w-e", 0, (250, 250)], ["b-e", 0, (300, 250)], ["w-e", 0, (350, 250)]],
    [["w-e", 0, (0, 300)], ["b-e", 0, (50, 300)], ["w-e", 0, (100, 300)], ["b-e", 0, (150, 300)],
     ["w-e", 0, (200, 300)], ["b-e", 0, (250, 300)], ["w-e", 0, (300, 300)], ["b-e", 0, (350, 300)]],
    [["b-e", 0, (0, 350)], ["w-e", 0, (50, 350)], ["b-e", 0, (100, 350)], ["w-e", 0, (150, 350)],
     ["b-e", 0, (200, 350)], ["w-e", 0, (250, 350)], ["b-e", 0, (300, 350)], ["w-e", 0, (350, 350)]],
    [["w-b", 0, (0, 400)], ["b-b", 0, (50, 400)], ["w-b", 0, (100, 400)], ["b-b", 0, (150, 400)],
     ["w-b", 0, (200, 400)], ["b-b", 0, (250, 400)], ["w-b", 0, (300, 400)], ["b-b", 0, (350, 400)]],
    [["b-b", 1, (0, 450)], ["w-b", 1, (50, 450)], ["b-b", 1, (100, 450)], ["w-b", 1, (150, 450)],
     ["b-b", 1, (200, 450)], ["w-b", 1, (250, 450)], ["b-b", 1, (300, 450)], ["w-b", 1, (350, 450)]],

]


def init():
    global screen, clock, pickedblack, pickedred
    pygame.init()
    pygame.mixer.init()
    pygame.display.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("checkers.py")
    clock = pygame.time.Clock()
    for root, dirs, files in os.walk("rec"):
        for name in files:
            print(f"importing {root}/{name}")
            if ".mp3" in name:
                audiorec.append(
                    [pygame.mixer.load(root+"/"+name), f"{name}".strip(".mp3")])
            elif ".png" in name:
                imgrec.append([pygame.image.load(root+"/"+name),
                              f"{name}".strip(".png")])
            else:
                print(f"unable to load file {root}/{name}")
    for img in imgrec:
        if img[1] == "sprite_p-r":
            pickedred = img[0]
        elif img[1] == "sprite_p-b":
            pickedblack = img[0]


init()
def drawcell(x, y, tile): return screen.blit(tile, (x, y))


puaseFlag = False

while running:
    # 1 Process input/events
    # clock.tick(FPS)  # will make the loop run at the same speed all the time
    # gets all the events which have occured till now and keeps tab of them.
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not puaseFlag:
            puaseFlag = True
        if event.type == pygame.MOUSEBUTTONUP and puaseFlag:
            if pickedFlag:
                if mousepos[1] > 100:
                    for row in board:
                        for col in row:
                            cellx, celly = col[2]
                            mousex, mousey = mousepos
                            if mousex >= col[2][0] and mousex <= col[2][0]+49:
                                if mousey >= col[2][1] and mousey <= col[2][1]+49:
                                    if col[0] == "b-e" or col[0] == "w-e":
                                        col[0] = f'{col[0][0]}-{picked}'
                                        picked = "e"

                                        pickedFlag = False
            elif not pickedFlag:
                if mousepos[1] > 100:
                    for row in board:
                        for col in row:
                            cellx, celly = col[2]
                            mousex, mousey = mousepos
                            if mousex >= col[2][0] and mousex <= col[2][0]+49:
                                if mousey >= col[2][1] and mousey <= col[2][1]+49:
                                    if col[0] != "b-e" or col[0] != "w-e":
                                        picked = col[0][2]
                                        col[0] = f'{col[0][0]}-e'
                                        col[1] = 0
                                        pickedFlag = True

        # listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    for img in imgrec:
        if img[1] == "sprite_banner":
            drawcell(0, 0, img[0])
    for row in board:
        for col in row:
            for tile in imgrec:
                if tile[1].split("sprite_")[1] == col[0]:
                    drawcell(col[2][0], col[2][1], tile[0])
            if col[1] == 1:
                for tile in imgrec:
                    if tile[1] == "sprite_crow":
                        drawcell(col[2][0], col[2][1], tile[0])

    if pickedFlag:
        print(f"picked! {picked}")
        if picked == "r":
            for row in board:
                for col in row:
                    cellx, celly = col[2]
                    mousex, mousey = mousepos
                    if mousex >= col[2][0] and mousex <= col[2][0]+49:
                        if mousey >= col[2][1] and mousey <= col[2][1]+49:
                            drawcell(cellx, celly,pickedred)
    pygame.display.flip()

pygame.quit()
