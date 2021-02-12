import pygame
from pygame.locals import *
from snake import Snake
import random


class MainApp:
    def __init__(self, width, height):
        # constructor of the MainApp Class
        self.run = True
        self.SIZE = self.WIDTH, self.HEIGHT = width, height 
        self.snake = Snake(width // 2, height // 2)
        self.food = {
            'x': random.randrange(0, self.WIDTH - Snake.WIDTH_UNIT, Snake.WIDTH_UNIT), 
            'y': random.randrange(0, self.HEIGHT - Snake.HEIGHT_UNIT, Snake.HEIGHT_UNIT)
            }

    def on_init(self):
        # initialize pygame and all modules

        # initialize the display 
        pygame.init()
        self.window = pygame.display.set_mode(self.SIZE)
        self.FPS = 10
        self.dx = 1
        self.dy = 0

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.dx = 0
                self.dy = -1
            if event.key == pygame.K_DOWN:
                self.dx = 0
                self.dy = 1
            if event.key == pygame.K_LEFT:
                self.dx = -1
                self.dy = 0
            if event.key == pygame.K_RIGHT:
                self.dx = 1
                self.dy = 0
    
    def on_loop(self):
        # the game loop
        # move the snake
        snake = self.snake.snake
        head = snake[0]
        new_Xpos = head.x + (Snake.WIDTH_UNIT * self.dx)
        new_YPos = head.y + (Snake.HEIGHT_UNIT * self.dy)

        if new_Xpos < self.WIDTH and  new_Xpos >= 0 and new_YPos < self.HEIGHT and new_YPos >= 0:
            queue = snake.pop(len(snake)-1)
            
            queue.x = new_Xpos
            queue.y = new_YPos
            snake.insert(0, queue)
        
        

    def on_render(self):
        # clean the window
        pygame.draw.rect(self.window, (0, 0, 0), pygame.rect.Rect(0, 0, self.WIDTH, self.HEIGHT))
        # render the snake
        
        for i, r in enumerate(self.snake.snake):
            if i == 0:
                pygame.draw.rect(self.window, (255, 0, 0), r)
            else:
                pygame.draw.rect(self.window, (255, 255, 255), r)

        # render the food
        rect_food = pygame.rect.Rect(self.food['x'], self.food['y'], Snake.WIDTH_UNIT-1, Snake.HEIGHT_UNIT-1)
        pygame.draw.rect(self.window, (255, 255, 255), rect_food)

        # update the window
        pygame.display.update()

    
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        # execute the game 
        if self.on_init() == False:
            sefl.run = False
        
        clock =  pygame.time.Clock();
        while self.run:
            print(self.dx, self.dy)
            clock.tick(self.FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    app = MainApp(640, 400)
    app.on_execute()