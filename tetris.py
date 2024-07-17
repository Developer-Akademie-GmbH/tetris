import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((200, 400))
tetrominos = [
    [(1, 5), (0, 4), (0, 5), (0, 6)],
    [(1, 5), (0, 5), (0, 6), (1, 6)],
    [(1, 4), (0, 4), (0, 5), (0, 6)],
    [(1, 6), (0, 4), (0, 5), (0, 6)],
    [(1, 5), (0, 4), (0, 5), (1, 6)],
    [(1, 5), (0, 5), (0, 6), (1, 4)],
    [(0, 4), (0, 5), (1, 5), (1, 6)]
]
colors = [
    (255, 0, 0),  # Rot
    (0, 255, 0),  # Grün
    (0, 0, 255),  # Blau
    (255, 255, 0),# Gelb
    (255, 0, 255),# Magenta
    (0, 255, 255),# Cyan
    (255, 165, 0) # Orange
]
grid = [[0] * 20 for _ in range(10)]
tetromino_color = random.choice(colors)

def is_valid_move(position, offset):
    for i in range(4):
        if position[i][1] + offset[1] < 0: continue
        if position[i][1] + offset[1] >= 20 or position[i][0] + offset[0] >= 10 or position[i][0] + offset[0] < 0: return 0
        if grid[position[i][0] + offset[0]][position[i][1] + offset[1]]: return 0
    return 1

def rotate(tetromino):
    cx, cy = tetromino[0][0], tetromino[0][1]  # Mittelpunkt des Tetrominos (pivot point)
    new_position = [(cx + cy - tetromino[i][1], cy - cx + tetromino[i][0]) for i in range(4)]
    if is_valid_move(new_position, [0, 0]): return new_position
    return tetromino

def get_random_tetromino():
    return tetrominos[random.randint(0, len(tetrominos) - 1)]

current_tetromino = get_random_tetromino()
movement_vector = [0, 1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: movement_vector = [-1, 0]
            if event.key == pygame.K_RIGHT: movement_vector = [1, 0]
            if event.key == pygame.K_UP: current_tetromino = rotate(current_tetromino)
        else: movement_vector = [0, 1]
    if not is_valid_move(current_tetromino, movement_vector):
        if movement_vector == [0, 1]:
            for i in range(4): 
                grid[current_tetromino[i][0]][current_tetromino[i][1]] = tetromino_color
            current_tetromino = get_random_tetromino()
            tetromino_color = random.choice(colors)
            if not is_valid_move(current_tetromino, [0, 0]): pygame.quit; sys.exit()
        movement_vector = [0, 0]
    


    screen.fill(pygame.Color('black'))
    for i in range(4):
        pygame.draw.rect(screen, tetromino_color, (current_tetromino[i][0] * 20, current_tetromino[i][1] * 20, 20, 20))
    current_tetromino = [(current_tetromino[i][0] + movement_vector[0], current_tetromino[i][1] + movement_vector[1]) for i in range(4)]
    
    for x in range(10):
        for y in range(20):
            if grid[x][y]:
                pygame.draw.rect(screen, grid[x][y], (x * 20, y * 20, 20, 20))
    pygame.display.flip()
    pygame.time.delay(100)