from typing import List, Tuple


def is_valid_sudoku(board: List[List[int | str]], custom_zones: List[List[Tuple[int, int]]]) -> bool:
   

    def has_unique_digits(values: List[int | str]) -> bool:
        
        seen = set()
        for val in values:
            if isinstance(val, str) and not val.isdigit():
                continue
            num = int(val)
            if not (1 <= num <= 9):
                return False
            if num in seen:
                return False
            seen.add(num)
        return True

    # Check rows
    for idx, row in enumerate(board):
        if not has_unique_digits(row):
            print(f"Row {idx} is invalid.")
            return False

    # Check columns
    for col_idx in range(9):
        col = [board[row_idx][col_idx] for row_idx in range(9)]
        if not has_unique_digits(col):
            print(f"Column {col_idx} is invalid.")
            return False

    # Check custom zones
    for zone_idx, zone in enumerate(custom_zones):
        zone_values = [board[r][c] for r, c in zone]
        if not has_unique_digits(zone_values):
            print(f"Zone {zone_idx} is invalid.")
            return False

    return True


def run_tests():
    # Test Case 1: Valid board
    board1 = [
        [5, 3, '.', '.', 7, '.', '.', '.', '.'],
        [6, '.', '.', 1, 9, 5, '.', '.', '.'],
        ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
        [8, '.', '.', '.', 6, '.', '.', '.', 3],
        [4, '.', '.', 8, '.', 3, '.', '.', 1],
        [7, '.', '.', '.', 2, '.', '.', '.', 6],
        ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
        ['.', '.', '.', 4, 1, 9, '.', '.', 5],
        ['.', '.', '.', '.', 8, '.', '.', 7, 9]
    ]

   
    zones = [
        [(r, c) for r in range(3) for c in range(3)],
        [(r, c) for r in range(3) for c in range(3, 6)],
        [(r, c) for r in range(3) for c in range(6, 9)],
        [(r, c) for r in range(3, 6) for c in range(3)],
        [(r, c) for r in range(3, 6) for c in range(3, 6)],
        [(r, c) for r in range(3, 6) for c in range(6, 9)],
        [(r, c) for r in range(6, 9) for c in range(3)],
        [(r, c) for r in range(6, 9) for c in range(3, 6)],
        [(r, c) for r in range(6, 9) for c in range(6, 9)],
    ]

    print("Test Case 1 (Valid Board):", "✅ Passed" if is_valid_sudoku(board1, zones) else "❌ Failed")

    # Test Case 2: Invalid row (duplicate 5)
    board2 = [row[:] for row in board1]
    board2[0][1] = 5  # Duplicate 5 in row 0
    print("Test Case 2 (Invalid Row):", "✅ Passed" if not is_valid_sudoku(board2, zones) else "❌ Failed")

    # Test Case 3: Invalid column (duplicate 9)
    board3 = [row[:] for row in board1]
    board3[1][0] = 5  # Duplicate 5 in column 0
    print("Test Case 3 (Invalid Column):", "✅ Passed" if not is_valid_sudoku(board3, zones) else "❌ Failed")

    # Test Case 4: Invalid custom zone (duplicate 6)
    board4 = [row[:] for row in board1]
    board4[0][0] = 6  # Will conflict with zone [1][1] which is also 6
    print("Test Case 4 (Invalid Zone):", "✅ Passed" if not is_valid_sudoku(board4, zones) else "❌ Failed")


if __name__ == "__main__":
    run_tests()

