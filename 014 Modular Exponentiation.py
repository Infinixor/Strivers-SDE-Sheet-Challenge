def modularExponentiation(x, n, m):
    # Declare a variable to store our result and initialize it with 1.
    answer = 1

    # Run a loop until 'N' > 0.
    while (n > 0):
        # If bitwise and of 'N' with 1 is 1 then multiply answer with 'X'.
        if (n & 1):
            answer = (answer * x) % m
        
        # Do modular squaring of 'X'.
        x = (x * x) % m

        # Right shift 'N' by 1 bit for the next iteration.
        n >>= 1

    # Return the answer.
    return answer

if __name__ == "__main__":
    # Test case 1
    x1, n1, m1 = 2, 10, 1000
    result1 = modularExponentiation(x1, n1, m1)
    print("Test case 1:")
    print("Expected output: 24")
    print("Actual output:", result1)
    print()

    # Test case 2
    x2, n2, m2 = 3, 5, 7
    result2 = modularExponentiation(x2, n2, m2)
    print("Test case 2:")
    print("Expected output: 5")
    print("Actual output:", result2)
