import pygame, sys, random, itertools
BLACK = (0, 0, 0)
GREY = (220, 220, 200) #Background
WHITE = (255, 255, 255) #Grid lines, dice text message background
PINK = (255, 0, 255) #Dice text message

#Lines
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#COLOURS = itertools.cycle([RED, GREEN, BLUE])
COLOURS = itertools.cycle([RED, BLUE])

windowSize = (800, 800)

def main():
    global SCREEN, CLOCK
    pygame.init()
    pygame.display.set_caption('Random Walk')
    SCREEN = pygame.display.set_mode(windowSize)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(GREY) #background

    #start in the middle of the grid
    currentPosition = [windowSize[0]//2, windowSize[1]//2 ]
    newPosition = currentPosition[:]

    arrow = pygame.image.load("images/arrow.png")
    arrow = pygame.transform.scale(arrow, (10, 10))
    arrowX, arrowY = currentPosition #tuple unpacking
    arrowSize = arrow.get_size()
    #pygame.draw.circle(SCREEN, BLACK, currentPosition, 6)
    
    myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

    drawGrid()
    currentGridScreen = SCREEN.copy()

    while True:
        CLOCK.tick(5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Generate the dice pair
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        #Load the dice message
        diceText = "Horizontal: %s, Vertical: %s" % (die1, die2)
        diceMessage = myriadProFont.render(diceText, 1, PINK, WHITE)
        diceMessageSize = diceMessage.get_size()
        SCREEN.blit(diceMessage, (windowSize[0]//2 - diceMessageSize[0]//2 , 0))
 
        #Horizontal line
        if die1 <= 3:
            newPosition[0] -= BLOCKSIZE
            arrowX -= BLOCKSIZE
        else:
            newPosition[0] += BLOCKSIZE
            arrowX += BLOCKSIZE
            
        if newPosition[0] < 0:
            newPosition[0] = 0
            arrowX = 0
        elif newPosition[0] > windowSize[0]:
            newPosition[0] = windowSize[0]
            arrowX = windowSize[0]
        
        SCREEN.fill(GREY)
        SCREEN.blit(currentGridScreen, (0, 0))
        pygame.draw.line(SCREEN, next(COLOURS), currentPosition, newPosition, 2)
        currentGridScreen = SCREEN.copy()
        SCREEN.blit(arrow, (arrowX, arrowY))
        pygame.draw.line(SCREEN, next(COLOURS), currentPosition, newPosition, 2)
        currentPosition = newPosition[:]
        pygame.display.update()
        
        #Vertical line
        if die2 <= 3:
            newPosition[1] -= BLOCKSIZE
            arrowY -= BLOCKSIZE
        else:
            newPosition[1] += BLOCKSIZE
            arrowY += BLOCKSIZE

        #if it goes out of boundaries
        if newPosition[1] < 0:
            newPosition[1] = 0
            arrowY = 0
        elif newPosition[1] > windowSize[1]:
            newPosition[1] = windowSize[1]
            arrowY = windowSize[1]
        
        SCREEN.fill(GREY)
        SCREEN.blit(currentGridScreen, (0, 0))
        pygame.draw.line(SCREEN, next(COLOURS), currentPosition, newPosition, 2)
        currentGridScreen = SCREEN.copy()
        SCREEN.blit(arrow, (arrowX, arrowY))
        currentPosition = newPosition[:]
        pygame.display.update()

def drawGrid():
    global BLOCKSIZE
    BLOCKSIZE = 40 #Set the size of the grid block - should be evenly divisible by window size
    for x in range(windowSize[0]):
        for y in range(windowSize[1]):
            rect = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

if __name__ == "__main__":
    main()
