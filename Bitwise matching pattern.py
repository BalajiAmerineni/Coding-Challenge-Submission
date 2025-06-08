def next_with_same_ones(n: int) -> int:
    """
    Returns the next larger integer with the same number of 1s in the binary representation.
    Uses bit manipulation based on Brian Kernighan’s algorithm.
    """

    c = n
    c0 = c1 = 0

   
    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    
    while (c & 1) == 1:
        c1 += 1
        c >>= 1

  
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1  
  
    p = c0 + c1

  
    n |= (1 << p)

   
    n &= ~((1 << p) - 1)

   
    n |= (1 << (c1 - 1)) - 1

    return n

def test_next_with_same_ones():
    test_cases = [
        (5, 6),      
        (6, 9),     
        (7, 11),   
        (1, 2),      
        (0, -1),     
        (15, 23),    
    ]

    for idx, (inp, expected) in enumerate(test_cases, 1):
        result = next_with_same_ones(inp)
        print(f"Test Case {idx}: Input = {inp} ({bin(inp)}), Output = {result} ({bin(result) if result != -1 else 'N/A'})")
        assert result == expected, f"Test {idx} failed!"

test_next_with_same_ones()

