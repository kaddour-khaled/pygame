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

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
    
    def on_loop(self):
        # the game loop
        pass

    def on_render(self):

        # render the snake
        for i, rect in enumerate(self.snake.snake):
            if i == 0:
                pygame.draw.rect(self.window, (255, 0, 0), rect)
            else:
                pygame.draw.rect(self.window, (255, 255, 255), rect)

        # render the food
        rect_food = pygame.rect.Rect(self.food['x'], self.food['y'], Snake.WIDTH_UNIT, Snake.HEIGHT_UNIT)
        pygame.draw.rect(self.window, (255, 255, 255), rect_food)

        # update the window
        pygame.display.update()

    
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        # execute the game 
        print("bbb")
        if self.on_init() == False:
            sefl.run = False
        
        while self.run:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()



if __name__ == "__main__":
    app = MainApp(640, 400)
    app.on_execute()