import pygame
import numpy as np
import math
import random

# Colors' initialization
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (230, 231, 232)
BLUEGREY = (132, 132, 130)
DARKGREY = (84, 84, 83)

# There are parameters of our window (initialization)
WIDTH = 800
HEIGHT = 800
# Set title
pygame.display.set_caption("Forth lab (group: 0323, team: 4)")
# Set window's parameters
window = pygame.display.set_mode((WIDTH, HEIGHT))

segments = []

xLeft = 200
xRight = 600
yDown = 200
yUp = 600

delta = 10

def addSegment():
    segments.append([(random.randint(0, WIDTH), random.randint(0, HEIGHT)), (random.randint(0, WIDTH), random.randint(0, HEIGHT))])

for i in range(10):
    addSegment()

def displaySurface():
    for i in range (xLeft, xRight, 1):
        pygame.draw.line(window, WHITE, (i, yDown), (i, yUp))
    pygame.draw.line(window, BLUE, (xLeft, yDown), (xLeft, yUp))
    pygame.draw.line(window, BLUE, (xLeft, yUp), (xRight, yUp))
    pygame.draw.line(window, BLUE, (xRight, yUp), (xRight, yDown))
    pygame.draw.line(window, BLUE, (xRight, yDown), (xLeft, yDown))

def isVisible(xStart, xFinal, yStart, yFinal):
    if (xStart < xLeft and xFinal < xLeft): return 0
    if (xStart > xRight and xFinal > xRight): return 0
    if (yStart < yDown and yFinal < yDown): return 0
    if (yStart > yUp and yFinal > yUp): return 0
    return 1

def isInView(x, y):
    check = 1
    if (x + check < xLeft): return 0
    if (x - check > xRight): return 0
    if (y + check < yDown): return 0
    if (y - check > yUp): return 0
    return 1

def ifFullyVisible(xStart, xFinal, yStart, yFinal):
    if (xStart <= xLeft or xStart >= xRight): return 0
    if (xFinal <= xLeft or xFinal >= xRight): return 0
    if (yStart <= yDown or yStart >= yUp): return 0
    if (yFinal <= yDown or yFinal >= yUp): return 0
    return 1

def drawParticallyVisibleSegment(x1, x2, y1, y2):
    tx1 = x1
    tx2 = x2
    ty1 = y1
    ty2 = y2

    deltaX = (x2 - x1)
    if (deltaX == 0): deltaX = 0.0001
    deltaY = (y2 - y1)
    if (deltaY == 0): deltaY = 0.0001

    t1 = (xLeft - x1) / deltaX
    if ((t1 >= 0 and t1 <= 1) and isInView(t1 * deltaX + x1, t1 * deltaY + y1)):
        if (isInView(tx1, ty1) == 0):
            tx1 = t1 * deltaX + x1
            ty1 = t1 * deltaY + y1
        elif (isInView(tx2, ty2) == 0):
            tx2 = t1 * deltaX + x1
            ty2 = t1 * deltaY + y1
    t2 = (xRight - x1) / deltaX
    if ((t2 >= 0 and t2 <= 1) and isInView(t2 * deltaX + x1, t2 * deltaY + y1)):
        if (isInView(tx1, ty1) == 0):
            tx1 = t2 * deltaX + x1
            ty1 = t2 * deltaY + y1
        elif (isInView(tx2, ty2) == 0):
            tx2 = t2 * deltaX + x1
            ty2 = t2 * deltaY + y1
    t3 = (yDown - y1) / deltaY
    if ((t3 >= 0 and t3 <= 1) and isInView(t3 * deltaX + x1, t3 * deltaY + y1)):
        if (isInView(tx1, ty1) == 0):
            tx1 = t3 * deltaX + x1
            ty1 = t3 * deltaY + y1
        elif (isInView(tx2, ty2) == 0):
            tx2 = t3 * deltaX + x1
            ty2 = t3 * deltaY + y1
    t4 = (yUp - y1) / deltaY
    if ((t4 >= 0 and t4 <= 1) and isInView(t4 * deltaX + x1, t4 * deltaY + y1)):
        if (isInView(tx1, ty1) == 0):
            tx1 = t4 * deltaX + x1
            ty1 = t4 * deltaY + y1
        elif (isInView(tx2, ty2) == 0):
            tx2 = t4 * deltaX + x1
            ty2 = t4 * deltaY + y1

    if (isInView(tx1, ty1) and isInView(tx2, ty2)):
        pygame.draw.line(window, GREEN, (tx1, ty1), (tx2, ty2), 3)

def displaySegments():
    for segment in segments:
        xStart = min(segment[0][0], segment[1][0])
        xFinal = max(segment[0][0], segment[1][0])
        yStart = min(segment[0][1], segment[1][1])
        yFinal = max(segment[0][1], segment[1][1])

        pygame.draw.line(window, DARKGREY, segment[0], segment[1])
        if (isVisible(xStart, xFinal, yStart, yFinal)):
            if (ifFullyVisible(xStart, xFinal, yStart, yFinal)):
                pygame.draw.line(window, GREEN, segment[0], segment[1], 3)
            else:
                drawParticallyVisibleSegment(segment[0][0], segment[1][0], segment[0][1], segment[1][1])


clock = pygame.time.Clock()

while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                yUp += delta
            if event.key == pygame.K_UP:
                yDown -= delta
            if event.key == pygame.K_RIGHT:
                xRight += delta
            if event.key == pygame.K_LEFT:
                xLeft -= delta
            if event.key == pygame.K_1:
                if (yDown + delta < yUp):
                    yUp -= delta
            if event.key == pygame.K_2:
                if (yDown + delta < yUp):
                    yDown += delta
            if event.key == pygame.K_3:
                if (xLeft + delta < xRight):
                    xRight -= delta
            if event.key == pygame.K_4:
                if (xLeft + delta < xRight):
                    xLeft += delta

    # Make window's color white
    window.fill(BLUEGREY)
    displaySurface()
    displaySegments()

    pygame.display.update()