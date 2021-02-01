import pygame

# initialize Global variabel

WIDTH, HEIGHT = 900, 500
UNIT_WIDTH = UNIT_HEIGHT = 50

HEAD_COLOR = (255, 0, 0)
BODY_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (255, 255, 255)


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_window():
    # draw window and objects


    rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
    pygame.draw.rect(WINDOW, BACKGROUND_COLOR, rect)
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_on_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()
