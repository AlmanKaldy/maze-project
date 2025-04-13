import random

def generate_maze(rows, cols):
    # Инициализация лабиринта: все клетки - стены
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    # Стартовая и конечная точки
    maze[0][0] = ' '  # стартовая точка
    maze[rows - 1][cols - 1] = ' '  # финишная точка

    # Список посещённых клеток
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Список для хранения возможных стен
    walls = []

    # Добавляем начальную точку в walls
    def add_wall(r, c):
        if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
            walls.append((r, c))

    add_wall(0, 0)

    while walls:
        # Случайным образом выбираем стенку
        wall = random.choice(walls)
        r, c = wall
        walls.remove(wall)

        # Определяем соседей этой клетки
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # вверх, вниз, влево, вправо
        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc]:
                    # Очищаем стену, если соседняя клетка ещё не посещена
                    maze[r][c] = ' '
                    visited[r][c] = True
                    add_wall(nr, nc)
                    break

    return maze
