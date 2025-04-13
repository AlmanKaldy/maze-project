from maze import generate_maze
from pathfinding import find_path

def main():
    rows, cols = 10, 10  # Размеры лабиринта
    maze = generate_maze(rows, cols)
    start = (0, 0)  # Точка старта (верхний левый угол)
    exit = (rows - 1, cols - 1)  # Точка выхода (нижний правый угол)
    
    print("Generated maze:")
    for row in maze:
        print("".join(row))

    path = None
    attempts = 0
    while not path and attempts < 10:  # Попробуем максимум 10 раз
        path = find_path(maze, start, exit)
        if not path:
            print("No path found. Regenerating maze...")
            maze = generate_maze(rows, cols)
            print("Generated maze again:")
            for row in maze:
                print("".join(row))
        attempts += 1

    if path:
        print("Path found:", path)
    else:
        print("No valid path found after multiple attempts.")

if __name__ == "__main__":
    main()
