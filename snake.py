import pygame

# snake : list[rect] 
# head: rect
# queue : rect
# lenght : int

class Snake:
    WIDTH_UNIT = 10
    HEIGHT_UNIT = 10
    MARGIN = 1
    INIT_LENGHT = 4

    def __init__(self, x, y):
        # initialize the snake
        self.snake = []
        for i in range(Snake.INIT_LENGHT):
            rectX = x - (i * Snake.WIDTH_UNIT)
            rectY = y
            rect = pygame.rect.Rect(
                rectX,
                rectY,
                Snake.WIDTH_UNIT-Snake.MARGIN,
                Snake.HEIGHT_UNIT- Snake.MARGIN
                )
            self.snake.append(rect)


        


