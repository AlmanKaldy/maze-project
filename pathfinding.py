def find_path(maze, start, exit):
    # Используем простой рекурсивный поиск с возвратом
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
