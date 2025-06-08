from collections import deque
from typing import List, Tuple

def bfs(grid: List[List[int]], start: Tuple[int, int]) -> List[List[int]]:
    """
    Performs BFS to calculate minimum steps from start to all other cells.
    """
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')] * m for _ in range(n)]
    q = deque([start])
    dist[start[0]][start[1]] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

def shortest_path_with_portal(grid: List[List[int]]) -> int:
    """
    Computes the shortest path from top-left to bottom-right using at most one teleport between any two empty cells.
    """
    n, m = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[n-1][m-1] == 1:
        return -1

    dist_start = bfs(grid, (0, 0))
    dist_end = bfs(grid, (n - 1, m - 1))

    min_path = dist_start[n - 1][m - 1]
    if min_path == float('inf'):
        min_path = -1

  
    min_teleport_path = float('inf')
    empty_cells = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0]

    for (x1, y1) in empty_cells:
        for (x2, y2) in empty_cells:
            if (x1, y1) == (x2, y2):
                continue
            path1 = dist_start[x1][y1]
            path2 = dist_end[x2][y2]
            if path1 != float('inf') and path2 != float('inf'):
                min_teleport_path = min(min_teleport_path, path1 + 1 + path2)

    result = min(min_path, min_teleport_path)
    return result if result != float('inf') else -1


def run_tests():
    grid1 = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    print("Test Case 1 (No teleport needed):", shortest_path_with_portal(grid1)) 

    grid2 = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    print("Test Case 2 (Teleport required):", shortest_path_with_portal(grid2)) 

    grid3 = [
        [0, 1],
        [1, 1]
    ]
    print("Test Case 3 (No path):", shortest_path_with_portal(grid3)) 

if __name__ == "__main__":
    run_tests()
