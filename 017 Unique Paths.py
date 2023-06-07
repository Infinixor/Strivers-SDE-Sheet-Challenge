def uniquePaths(m, n):
    # Reference array to store subproblems.
    dp = [0 for _ in range(n)]
    dp[0] = 1

    # Bottom-up approach.
    for _ in range(m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    # Returning answer.
    return dp[n - 1]


if __name__ == "__main__":
    # Test case 1
    m1 = 3
    n1 = 7
    result1 = uniquePaths(m1, n1)
    print("Test case 1:")
    print("Expected output: 28")
    print("Actual output:", result1)
    print()

    # Test case 2
    m2 = 3
    n2 = 2
    result2 = uniquePaths(m2, n2)
    print("Test case 2:")
    print("Expected output: 3")
    print("Actual output:", result2)
