from typing import List, Dict, Set
from collections import defaultdict, deque

def alien_order(words: List[str]) -> str:
    """
    Given a sorted list of words from an alien dictionary, return the correct order of characters.

    Args:
        words (List[str]): List of words sorted lexicographically in alien language.

    Returns:
        str: A string representing the correct character order in the alien language.
    """
   
    graph: Dict[str, Set[str]] = defaultdict(set)
    in_degree: Dict[str, int] = {char: 0 for word in words for char in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
           
            return ""

        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break

  
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) < len(in_degree):
        
        return ""

    return "".join(order)

#Test Cases

def run_tests():
    print("Test Case 1:")
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    print("Input:", words1)
    print("Output:", alien_order(words1))  
    print()

    print("Test Case 2:")
    words2 = ["z", "x"]
    print("Input:", words2)
    print("Output:", alien_order(words2))  
    print()

    print("Test Case 3:")
    words3 = ["z", "x", "z"]
    print("Input:", words3)
    print("Output:", alien_order(words3)) 
    print()

if __name__ == "__main__":
    run_tests()

