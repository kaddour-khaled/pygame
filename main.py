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

    def on_init(self):
        # initialize pygame and all modules

        # initialize the display 
        pygame.init()
        pygame.font.init()
        self.lose = False
        self.USER_EVENT = pygame.USEREVENT + 1
        self.window = pygame.display.set_mode(self.SIZE)
        self.FPS = 10
        self.dx = 1
        self.dy = 0
        self.FONT = pygame.font.SysFont("comicsans", 40)
        self.food = pygame.rect.Rect(
            random.randrange(0, self.WIDTH - Snake.WIDTH_UNIT, Snake.WIDTH_UNIT),
            random.randrange(0, self.HEIGHT - Snake.HEIGHT_UNIT, Snake.HEIGHT_UNIT),
            Snake.WIDTH_UNIT-1,
            Snake.HEIGHT_UNIT-1
            )

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == self.USER_EVENT:
            self.lose = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.dy == 0:
                self.dx = 0
                self.dy = -1
            if event.key == pygame.K_DOWN and self.dy == 0:
                self.dx = 0
                self.dy = 1
            if event.key == pygame.K_LEFT and self.dx == 0:
                self.dx = -1
                self.dy = 0
            if event.key == pygame.K_RIGHT and self.dx == 0:
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
            if queue.collidelist(snake) > 0:
                pygame.event.post(pygame.event.Event(self.USER_EVENT))
            snake.insert(0, queue)

        else:
            pygame.event.post(pygame.event.Event(self.USER_EVENT))
        
    
        
        # handel the collision of snake with food
        if head.colliderect(self.food):
            queue = snake[len(snake)- 1]
            b_queue = snake[len(snake)- 2]
            new_rect = pygame.rect.Rect(queue.x, queue.y, Snake.WIDTH_UNIT-1, Snake.HEIGHT_UNIT - 1)
            
            if queue.x == b_queue.x:
                new_rect.y += queue.y - b_queue.y

            if queue.y == b_queue.y:
                new_rect.x += queue.x - b_queue.x
            snake.append(new_rect)

            self.food = pygame.rect.Rect(
            random.randrange(0, self.WIDTH - Snake.WIDTH_UNIT, Snake.WIDTH_UNIT),
            random.randrange(0, self.HEIGHT - Snake.HEIGHT_UNIT, Snake.HEIGHT_UNIT),
            Snake.WIDTH_UNIT-1,
            Snake.HEIGHT_UNIT-1
            )
            
        

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
        pygame.draw.rect(self.window, (255, 255, 255), self.food)
        
        # render text (score + lose text) 
        Score  = self.FONT.render("Score : " + str(len(self.snake.snake) - Snake.INIT_LENGHT), 1, (255, 255, 255))
        self.window.blit(
            Score,
            (self.WIDTH - Score.get_width()-10, 10)
            )

        # render lose text
        if self.lose:
            lose_text  = self.FONT.render("You lose :(" , 1, (255, 255, 255))
            self.window.blit(
                lose_text,
                (self.WIDTH//2 - Score.get_width()//2, self.HEIGHT//2 - Score.get_height()//2)
                )
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
            
            clock.tick(self.FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            if self.lose:
                pygame.time.delay(2000)
                self.run = False
        self.on_cleanup()


if __name__ == "__main__":
    app = MainApp(640, 400)
    app.on_execute()