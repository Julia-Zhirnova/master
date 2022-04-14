import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count, snake_speed = 0, 10

pygame.init()
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
imgbg = pygame.image.load('moon.jpg').convert()

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:
    surface.blit(imgbg, (0, 0))

    # drawing snake, apple
    
    
    #rect.center = (200, 300)
    #surface.blit(img, pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE)))
    img_lun = pygame.image.load("1.png")
    for i, j in snake:
        lunokhod = pygame.draw.rect(surface,pygame.Color('white'), (i, j, SIZE - 1, SIZE - 1))
    #lunokhod = [pygame.draw.rect(surface,pygame.Color('white'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
        scaled_img = pygame.transform.scale(img_lun, lunokhod.size)
        scaled_img = scaled_img.convert()
        surface.blit(scaled_img, lunokhod)

    img_alian = pygame.image.load("alian.png")
    rect = pygame.draw.rect(surface, pygame.Color('white'),(*apple, SIZE, SIZE))
    scaled_img = pygame.transform.scale(img_alian, rect.size)
    scaled_img = scaled_img.convert()
    surface.blit(scaled_img, rect)
    
    # show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))
    # snake movement
    speed_count += 1
    if not speed_count % snake_speed:
	    x += dx * SIZE
	    y += dy * SIZE
	    snake.append((x, y))
	    snake = snake[-length:]
    # eating food
    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)
    # game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()

    pygame.display.flip()
    clock.tick(fps)
    close_game()
    # controls
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }




