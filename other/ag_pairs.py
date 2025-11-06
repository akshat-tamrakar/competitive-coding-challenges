"""
AG Pairs Counter
Problem: Count the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j
"""

def count_ag_pairs(A: str) -> int:
    a_count = 0
    total_pairs = 0
    
    for char in A:
        if char == 'A':
            a_count += 1
        elif char == 'G':
            total_pairs += a_count
    
    return total_pairs
    

if __name__ == "__main__":
    test_cases = [
        ("ABCGAG", 3),  # Pairs: (0,3), (0,5), (4,5)
        ("GAB", 0),     # No valid pairs
        ("AAG", 2),     # Pairs: (0,2), (1,2)
        ("AGG", 2),     # Pairs: (0,1)
        ("AAAGGG", 9)   # Pairs: (0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)
    ]
    
    # Run test cases and verify results
    for test_str, expected in test_cases:
        result = count_ag_pairs(test_str)
        print(f"Input: {test_str:8} | Expected: {expected:2} | Got: {result:2} | "
              f"{'✓' if result == expected else '✗'}")