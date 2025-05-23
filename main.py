from maze import generate_maze
from pathfinding import find_path

def main():
    rows, cols = 10, 20  # Размеры лабиринта
    maze = generate_maze(rows, cols)
    start = (0, 0)  # Точка старта (верхний левый угол)
    exit = (rows - 1, cols - 1)  # Точка выхода (нижний правый угол)
    
    print("Generated maze:")
    for row in maze:
        print("".join(row))
    
    path = find_path(maze, start, exit)
    if path:
        print("Path found:", path)
        # Отображаем путь в лабиринте
        for (x, y) in path:
            if (x, y) != start and (x, y) != exit:
                maze[x][y] = '.'  # Отображаем путь
    else:
        print("No path found. Regenerating maze...")
        return  # Возвращаемся, если путь не найден
    
    # Выводим лабиринт с отображенным путем
    print("Maze with path:")
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    main()
