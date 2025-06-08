def next_with_same_ones(n: int) -> int:
    """
    Returns the next larger integer with the same number of 1s in the binary representation.
    Uses bit manipulation based on Brian Kernighan’s algorithm.
    """

    c = n
    c0 = c1 = 0

    # Count trailing 0s (c0)
    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    # Count 1s after trailing 0s (c1)
    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    # If n == 111...0000 (e.g., all 1s followed by 0s), no bigger number with same bits
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1  # Not possible

    # Position of rightmost non-trailing zero
    p = c0 + c1

    # Step 1: Flip rightmost non-trailing 0
    n |= (1 << p)

    # Step 2: Clear all bits to the right of p
    n &= ~((1 << p) - 1)

    # Step 3: Insert (c1-1) ones on the right
    n |= (1 << (c1 - 1)) - 1

    return n

def test_next_with_same_ones():
    test_cases = [
        (5, 6),      # 101 -> 110
        (6, 9),      # 110 -> 1001
        (7, 11),     # 111 -> 1011
        (1, 2),      # 0001 -> 0010
        (0, -1),     # No 1s to match
        (15, 23),    # 1111 -> 10111
    ]

    for idx, (inp, expected) in enumerate(test_cases, 1):
        result = next_with_same_ones(inp)
        print(f"Test Case {idx}: Input = {inp} ({bin(inp)}), Output = {result} ({bin(result) if result != -1 else 'N/A'})")
        assert result == expected, f"Test {idx} failed!"

test_next_with_same_ones()

