"""
@author: Infinixor
"""

# Swapping two alphabets in a string.
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def findPermutationsHelper(lst, i, j, ans):
    if i >= j:
        # Storing the string in the vector ans.
        permutation = ""

        for k in range(len(lst)):
            permutation += lst[k]

        ans.append(permutation)
        return

    # Fixing a character at index i and then swapping with characters from index i to j and by this way building up permutation strings.
    for k in range(i, j + 1):
        swap(lst, i, k)
        findPermutationsHelper(lst, i + 1, j, ans)
        swap(lst, i, k)


def findPermutations(s):
    # Declaring a vector of strings to store all the possible permutations of the string.
    ans = []
    lst = list(s)
    # Calling the user-defined function which stores all the possible permutations of the string in the vector ans.
    findPermutationsHelper(lst, 0, len(lst) - 1, ans)
    return ans


def main():
    # Example usage
    input_string = "abc"
    result = findPermutations(input_string)
    print("All permutations of", input_string + ":", result)


if __name__ == "__main__":
    main()
