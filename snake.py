import pygame

# initialize Global variabel

WIDTH, HEIGHT = 900, 500
UNIT_WIDTH = UNIT_HEIGHT = 15

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

    snake = init_snake();
    while run:
        # handel the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(snake)
    
    pygame.quit()

if __name__ == "__main__":
    main()
