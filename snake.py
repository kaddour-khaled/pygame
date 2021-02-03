import pygame
import random

# initialize Global variabel

WIDTH, HEIGHT = 900, 510
UNIT_WIDTH = UNIT_HEIGHT = 10
FPS = 5

BASE_LENGTH_SNAKE = 4

LOSE_EVENT = pygame.USEREVENT + 1


HEAD_COLOR = (255, 0, 0)
BODY_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (255, 255, 255)


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def init_snake():
    # create and initialize the snake
    start_x_postion = WIDTH // 2 + (UNIT_WIDTH * BASE_LENGTH_SNAKE) // 2
    start_y_postion = HEIGHT //2 - UNIT_HEIGHT // 2

    snake = []

    for i in range(BASE_LENGTH_SNAKE):
        rect = pygame.rect.Rect(start_x_postion - (UNIT_WIDTH*i), start_y_postion, UNIT_HEIGHT -1 , UNIT_HEIGHT-1)
        snake.append(rect)

    return snake     

def move_snake(snake, DX, DY):
    # move the snake
    # remove the queue of the snake (index = len(snake) -1) and add to the head of the snake (index = 0)
    
    
    old_head = snake[0]

    new_x_pos = old_head.x + (UNIT_WIDTH * DX)
    new_y_pos = old_head.y + (UNIT_HEIGHT * DY)

    if new_x_pos < 0 or new_y_pos < 0 or new_x_pos + UNIT_WIDTH > WIDTH or new_y_pos + UNIT_HEIGHT > HEIGHT:
        pygame.event.post(pygame.event.Event(LOSE_EVENT))
    else:
        new_head = snake.pop(len(snake)-1)
        new_head.x = new_x_pos
        new_head.y = new_y_pos
        snake.insert(0, new_head)
         
def create_random_food():
    # create food in window
    x, y = random.randrange(0, WIDTH-UNIT_WIDTH, UNIT_WIDTH), random.randrange(0, HEIGHT-UNIT_HEIGHT, UNIT_HEIGHT)
    return pygame.rect.Rect(x, y, UNIT_WIDTH-1, UNIT_HEIGHT-1)

def detect_collision(snake, food, dx, dy):
    # eat food
    if food.colliderect(snake[0]):
        queue = snake[len(snake)-1]
        if dx > 0:
            food.x = queue.x - UNIT_WIDTH
        if dx < 0:
            food.x = queue.x + UNIT_WIDTH
        if dy > 0:
            food.y = queue.y - UNIT_HEIGHT
        if dy < 0:
            food.y = queue.y + UNIT_HEIGHT
        snake.append(food)
        food = create_random_food()
    return food

def draw_window(snake, food):
    # draw window and objects

    # clean the window
    rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
    pygame.draw.rect(WINDOW, BACKGROUND_COLOR, rect)
    
    # draw the snake on the window
    for (i, r) in enumerate(snake):
        if i == 0:
            pygame.draw.rect(WINDOW, HEAD_COLOR, r)
           
        else:
            pygame.draw.rect(WINDOW, BODY_COLOR, r)

    # draw food
    pygame.draw.rect(WINDOW, HEAD_COLOR, food)
    # update the window
    pygame.display.update()

def main():
    # man function
    run = True
    clock = pygame.time.Clock()

    snake = init_snake()
    food = create_random_food()
    DX, DY = 1, 0

    while run:
        clock.tick(FPS)

        # handel the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and DY == 0:
                    DY = -1
                    DX = 0
                if event.key == pygame.K_DOWN and DY == 0:
                    DY = 1
                    DX= 0
                if event.key == pygame.K_LEFT and DX == 0:
                    DX = -1
                    DY = 0
                if event.key == pygame.K_RIGHT and DX == 0:
                    DX = 1
                    DY = 0
            if event.type == LOSE_EVENT:
                print("lose")
                pygame.time.delay(1000)
                run = False  
        move_snake(snake, DX, DY)
        food = detect_collision(snake, food, DX, DY)
        draw_window(snake, food)
    
    pygame.quit()

if __name__ == "__main__":
    main()
