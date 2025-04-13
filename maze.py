import random

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    # Стартовая и конечная точки
    maze[0][0] = ' '  # стартовая точка
    maze[rows - 1][cols - 1] = ' '  # финишная точка
    
    # Генерация пути с использованием алгоритма рекурсивного возврата
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
