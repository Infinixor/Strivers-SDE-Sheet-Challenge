def nextPermutation(permutation, n):
    n = len(permutation)

    # Start iterating from the end of the given permutation.
    for i in range(n - 2, -1, -1):
        if permutation[i] < permutation[i + 1]:
            # Decreasing element found.
            # To store the index of just greater element.
            index = n - 1

            for j in range(i + 1, n):
                if permutation[j] < permutation[i]:
                    # Element found.
                    index = j - 1
                    break

            # Swap the ith and element at index 'index'.
            permutation[i], permutation[index] = permutation[index], permutation[i]

            # Reverse rest of the elements.
            for j in range(((n - i) // 2)):
                permutation[i + 1 + j], permutation[n - 1 - j] = permutation[n - 1 - j], permutation[i + 1 + j]

            return permutation

    # Next greater permutation doesn't exist. So, return the smallest one.
    permutation = [i for i in range(1, n + 1)]

    return permutation


def main():
    # Test Case 1
    permutation = [1, 2, 3]
    n = len(permutation)
    print(f"Original Permutation: {permutation}")
    next_permutation = nextPermutation(permutation, n)
    print(f"Next Permutation: {next_permutation}")
    print()

    # Test Case 2
    permutation = [3, 2, 1]
    n = len(permutation)
    print(f"Original Permutation: {permutation}")
    next_permutation = nextPermutation(permutation, n)
    print(f"Next Permutation: {next_permutation}")
    print()

    # Test Case 3
    permutation = [1, 1, 5]
    n = len(permutation)
    print(f"Original Permutation: {permutation}")
    next_permutation = nextPermutation(permutation, n)
    print(f"Next Permutation: {next_permutation}")
    print()


if __name__ == "__main__":
    main()
