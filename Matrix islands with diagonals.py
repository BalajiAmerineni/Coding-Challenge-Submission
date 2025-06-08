from typing import List

def count_islands(matrix: List[List[int]]) -> int:
    """
    Counts the number of islands in the matrix.
    An island is a group of connected 1s (connected in 8 directions).
    """

    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # All 8 possible directions: horizontal, vertical, and diagonals
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    def dfs(r: int, c: int):
        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows and
                0 <= nc < cols and
                not visited[nr][nc] and
                matrix[nr][nc] == 1
            ):
                dfs(nr, nc)

    island_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                island_count += 1

    return island_count

def test_count_islands():
    print("Test Case 1:")
    mat1 = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0]
    ]
    print("Islands Count:", count_islands(mat1))  # Expected: 3

    print("\nTest Case 2:")
    mat2 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print("Islands Count:", count_islands(mat2))  # Expected: 1 (all connected diagonally)

    print("\nTest Case 3:")
    mat3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print("Islands Count:", count_islands(mat3))  # Expected: 0

test_count_islands()
