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
    
    path = find_path(maze, start, exit)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
