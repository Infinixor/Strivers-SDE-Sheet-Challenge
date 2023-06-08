"""
@author: Infinixor
"""

def kthPermutation(n, k):
    factorial = 1
    s = ""

    for i in range(1, n + 1):
        factorial *= i

        # Build a string of the sequence 1234...n.
        s += str(i)

    k -= 1

    for i in range(n):
        factorial //= n - i
        # Calculate the index of the character to put at index i in 's'.
        j = i + k // factorial
        c = s[j]

        # Remove c by shifting to cover up (adjust the right part).
        while j > i:
            s = s[:j] + s[j - 1] + s[j + 1:]
            j -= 1

        k %= factorial
        s = s[:i] + c + s[i + 1:]

    return s


def main():
    # Example usage
    n = 4
    k = 9
    result = kthPermutation(n, k)
    print(f"The {k}th permutation of numbers from 1 to {n}: {result}")


if __name__ == "__main__":
    main()
