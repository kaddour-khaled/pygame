import pygame

# initialize Global variabel

WIDTH, HEIGHT = 900, 500
UNIT_WIDTH = UNIT_HEIGHT = 15
FPS = 10 

BASE_LENGTH_SNAKE = 4



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
    
    new_head = snake.pop(len(snake)-1)
    old_head = snake[0]

    new_head.x = old_head.x+(UNIT_WIDTH * DX)
    new_head.y = old_head.y+ (UNIT_HEIGHT * DY)

    snake.insert(0, new_head)

def draw_window(snake):
    # draw window and objects

    # clean the window
    rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
    pygame.draw.rect(WINDOW, BACKGROUND_COLOR, rect)
    
    # draw the snake on the window
    for (i, r) in enumerate(snake):
        if i == 0:
            pygame.draw.rect(WINDOW, HEAD_COLOR, r, 0)
           
        else:
            pygame.draw.rect(WINDOW, BODY_COLOR, r, 0)

    # update the window
    pygame.display.update()

def main():
    # man function
    run = True
    clock = pygame.time.Clock()

    snake = init_snake();
    DX, DY = 1, 0

    while run:
        clock.tick(FPS)

        # handel the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and DY == 0:
                    print("up")
                    DY = -1
                    DX = 0
                if event.key == pygame.K_DOWN and DY == 0:
                    print("down")
                    DY = 1
                    DX= 0
                if event.key == pygame.K_LEFT and DX == 0:
                    print("left")
                    DX = -1
                    DY = 0
                if event.key == pygame.K_RIGHT and DX == 0:
                    print("right")
                    DX = 1
                    DY = 0  
        move_snake(snake, DX, DY)
        draw_window(snake)
    
    pygame.quit()

if __name__ == "__main__":
    main()
