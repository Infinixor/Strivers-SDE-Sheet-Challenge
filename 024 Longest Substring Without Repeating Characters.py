def uniqueSubstrings(input):
    n = len(input)
    Set = set()
    ans = 0
    i = 0
    j = 0
    while i < n and j < n:
        # Try to extend the range [i,j]
        if input[j] not in Set:
            Set.add(input[j])
            ans = max(ans, j - i + 1)
            j += 1
        else:
            Set.remove(input[i])
            i += 1
    return ans


def main():
    # Test Case 1
    input1 = "abcabcbb"
    print(f"Input: {input1}")
    print(f"Longest unique substring length: {uniqueSubstrings(input1)}")

    # Test Case 2
    input2 = "bbbbb"
    print(f"\nInput: {input2}")
    print(f"Longest unique substring length: {uniqueSubstrings(input2)}")


if __name__ == "__main__":
    main()
