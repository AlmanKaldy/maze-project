import pygame
import random

# Размеры окна и клеток
CELL_SIZE = 30
WIDTH = 600
HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Инициализация pygame
pygame.init()

# Функция для генерации лабиринта
def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = ' '  # Старт
    maze[rows - 1][cols - 1] = ' '  # Финиш
    
    def carve_path(r, c):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr * 2, c + dc * 2
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '#':
                maze[nr][nc] = ' '
                maze[r + dr][c + dc] = ' '
                carve_path(nr, nc)

    carve_path(0, 0)
    return maze

# Функция для поиска пути
def find_path(maze, start, exit):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(x, y, path):
        if (x, y) == exit:
            return path
        
        visited[x][y] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # вправо, вниз, влево, вверх
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] == ' ':
                result = dfs(nx, ny, path + [(nx, ny)])
                if result:
                    return result
        
        return None  # Путь не найден

    return dfs(start[0], start[1], [start])

# Функция для отображения лабиринта и пути с использованием Pygame
def display_maze_with_path(maze, path):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Visualization")

    running = True
    while running:
        screen.fill(WHITE)
        
        # Рисуем лабиринт
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                color = BLACK if maze[i][j] == '#' else WHITE
                pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                
        # Рисуем путь
        if path:
            for (x, y) in path:
                pygame.draw.rect(screen, YELLOW, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        # Обновляем экран
        pygame.display.flip()

        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

# Главная функция
def main():
    rows, cols = 10, 10  # Размер лабиринта
    maze = generate_maze(rows, cols)
    start = (0, 0)  # Точка старта
    exit = (rows - 1, cols - 1)  # Точка выхода

    # Ищем путь
    path = find_path(maze, start, exit)

    # Если путь найден, выводим лабиринт с путем
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
    
    # Отображаем лабиринт с путем
    display_maze_with_path(maze, path)

if __name__ == "__main__":
    main()
