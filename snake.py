import sys
import time
import random
#---------------------------------------------------------------------#
import pygame
pygame.init()


# snake class
class Snake(object):
    def __init__(self,x_coord,y_coord,vel,color):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.vel = vel
        self.color = color
        self.snakeList = []

    def draw_snake(self):
        pygame.draw.rect(window, self.color, [self.x_coord,self.y_coord,10,10])

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

# window settings # TODO: set function for settings
SCREEN_SIZE = (600,600)
pygame.display.set_caption("Snake Game")
window = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

## TODO: problem is the more elements we have in the list, the same amount
# of elements will be added or substrated from the obj.x_coord and obj.y_coord
def main_snake(obj, snakeList):
    for elem in snakeList:
        obj.draw_snake()
        obj.x_coord += elem[0]
        obj.y_coord += elem[1]
    list_of_coodinates = [obj.x_coord,obj.y_coord]
    return list_of_coodinates


# screen message function
def message_to_screen(msg,color):

    font = pygame.font.SysFont(None, 25)

    text = font.render(msg, True, color)

    window.blit(text, [(SCREEN_SIZE[0]/2)-160,SCREEN_SIZE[1]/2])


#------------------------------Main game LOOP------------------------------#
def gameLoop():
    snakeList = []
    snakeLenght = 1
    #start point snake object
    vel = 10
    #start point snake object + (starting coordinates) + vel + color
    snake = Snake((SCREEN_SIZE[0]/2),(SCREEN_SIZE[1]/2),vel,green)
    snakeTail = Snake((SCREEN_SIZE[0]/2),(SCREEN_SIZE[1]/2),vel,green)
    FPS = 15
    done = False
    gameOver = False
    x_move = 0
    y_move = 0
    pygame.display.update()
    randXapple = random.randrange(0,(SCREEN_SIZE[0] - vel), vel)
    randYapple = random.randrange(0,(SCREEN_SIZE[1] - vel), vel)

    while not done:
        #game over handling
        while gameOver == True:
            window.fill(black)
            message_to_screen("GAMEOVER!,'C' to play again, 'Q' to QUIT game ", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        done = True
                    if event.key == pygame.K_c:
                        gameLoop()

        # main event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # controllers + game logic
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -(vel)
                    y_move = 0
                elif event.key == pygame.K_RIGHT:
                    x_move = vel
                    y_move = 0
                elif event.key == pygame.K_UP:
                    y_move = -(vel)
                    x_move = 0
                elif event.key == pygame.K_DOWN:
                    y_move = vel
                    x_move = 0
        window.fill(black)
        # load apples
        pygame.draw.rect(window,red,[randXapple,randYapple,10,10])

        # main_snake() draw snake, takes object snake and a list with coords
        snakeHead = []
        snakeHead.append(x_move)
        snakeHead.append(y_move)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLenght:
            del snakeList[0]
        coodinates = main_snake(snake,snakeList)

        # send user to a func where he decides to close game or not
        if snake.x_coord >= SCREEN_SIZE[0] or snake.x_coord < 0 \
            or snake.y_coord >= SCREEN_SIZE[1] or snake.y_coord < 0:
            gameOver = True

        if coodinates[0] == randXapple and coodinates[1] == randYapple:
            randXapple = random.randrange(0,(SCREEN_SIZE[0]-vel),vel)
            randYapple = random.randrange(0,(SCREEN_SIZE[1]-vel),vel)
            snakeLenght += 1
    
        pygame.display.update()
        # frames/sec
        clock.tick(FPS)

    # exit game property
    pygame.quit()
    quit()


gameLoop()
