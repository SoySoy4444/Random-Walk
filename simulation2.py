import pygame, sys, random, itertools
BLACK = (0, 0, 0)
GREY = (220, 220, 200) #Background
WHITE = (255, 255, 255) #Grid lines, dice text message background
PINK = (255, 0, 255) #Dice text messages
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN= (150, 75, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHTBLUE = (173, 216, 230)
LIGHTGREEN = (144, 238, 144)

windowSize = (800, 800)

def main():
    colourSchemes = [
        itertools.cycle([RED, BLUE]), 
        itertools.cycle([GREEN, RED, BLUE]),
        itertools.cycle([RED, BROWN]),
        itertools.cycle([BLACK, YELLOW]),
        itertools.cycle([GREEN, ORANGE]),
        itertools.cycle([YELLOW, BLUE]),
        itertools.cycle([BLUE, PINK]),
        itertools.cycle([LIGHTGREEN, LIGHTBLUE, GREEN]),
        itertools.cycle([LIGHTBLUE, ORANGE]),
    ]
    COLOURS = colourSchemes[0] #default colour
    framesPerSecond = 5 #default speed
    BLOCKSIZE = 40 #default grid size
    
    def pause():
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c: #if c pressed, Continue playing
                        paused = False
                    elif event.key == pygame.K_r: #reset
                        reset()
                        paused = False
            pygame.display.update()
            clock.tick(5)
    
    def drawGrid(blockSize):
        screen.fill(GREY) #background
        blockSize = 40 #Set the size of the grid block - should be evenly divisible by window size
        for x in range(windowSize[0]):
                for y in range(windowSize[1]):
                    rect = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
                    pygame.draw.rect(screen, WHITE, rect, 1)
        return screen.copy()
        
    def reset(blockSize):
        currentGridScreen = drawGrid(blockSize) #draw initial grid
        
        currentPosition = [windowSize[0]//2, windowSize[1]//2 ]
        newPosition = currentPosition[:]
        
        arrowX, arrowY = currentPosition #tuple unpacking
        
        return (currentGridScreen, currentPosition, newPosition, arrowX, arrowY)

    pygame.init()
    pygame.display.set_caption('Random Walk')
    screen = pygame.display.set_mode(windowSize)
    clock = pygame.time.Clock()

    arrow = pygame.image.load("arrow.png")
    arrow = pygame.transform.scale(arrow, (10, 10))
    
    myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

    currentGridScreen, currentPosition, newPosition, arrowX, arrowY = reset(BLOCKSIZE)

    while True:
        clock.tick(framesPerSecond)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: #pause
                    pause()
                elif event.key == pygame.K_r: #reset
                    currentGridScreen, currentPosition, newPosition, arrowX, arrowY = reset(BLOCKSIZE)
                elif event.key == pygame.K_UP: #speed up
                    framesPerSecond += 1
                elif event.key == pygame.K_DOWN: #slow down
                    if framesPerSecond != 1: #FPS cannot be 0 or negative.
                        framesPerSecond -= 1
                elif event.key == pygame.K_1:
                    COLOURS = colourSchemes[0]
                elif event.key == pygame.K_2:
                    COLOURS = colourSchemes[1]
                elif event.key == pygame.K_3:
                    COLOURS = colourSchemes[2]
                elif event.key == pygame.K_4:
                    COLOURS = colourSchemes[3]
                elif event.key == pygame.K_5:
                    COLOURS = colourSchemes[4]
                elif event.key == pygame.K_6:
                    COLOURS = colourSchemes[5]
                elif event.key == pygame.K_7:
                    COLOURS = colourSchemes[6]
                elif event.key == pygame.K_8:
                    COLOURS = colourSchemes[7]
                elif event.key == pygame.K_9:
                    COLOURS = colourSchemes[8]
        #Generate the dice pair
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        #Load the dice message
        diceText = "Horizontal: %s, Vertical: %s" % (die1, die2)
        diceMessage = myriadProFont.render(diceText, 1, BLACK, WHITE)
        diceMessageSize = diceMessage.get_size()
 
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
        
        screen.fill(GREY)
        screen.blit(currentGridScreen, (0, 0))
        pygame.draw.line(screen, next(COLOURS), currentPosition, newPosition, 2)
        screen.blit(diceMessage, (windowSize[0]//2 - diceMessageSize[0]//2 , 0))
        currentGridScreen = screen.copy()
        screen.blit(arrow, (arrowX, arrowY))
        currentPosition = newPosition[:]
        pygame.display.update()
        
        clock.tick(framesPerSecond)
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
        
        screen.fill(GREY)
        screen.blit(currentGridScreen, (0, 0))
        pygame.draw.line(screen, next(COLOURS), currentPosition, newPosition, 2)
        screen.blit(diceMessage, (windowSize[0]//2 - diceMessageSize[0]//2 , 0))
        currentGridScreen = screen.copy()
        screen.blit(arrow, (arrowX, arrowY))
        currentPosition = newPosition[:]
        pygame.display.update()

if __name__ == "__main__":
    main()