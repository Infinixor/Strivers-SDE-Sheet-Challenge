"""
@author: Infinixor
"""

def findSubsetsThatSumToK(arr, n, k):
    # Ans vector contains all the subset which sum up to 'K'.
    ans = [[]]

    for i in range(0, 1 << n):
        total_sum = 0
        subset = []
        for j in range(n):
            # Checking whether the element is present in the subset or not.
            if (1 << j) & i:
                total_sum += arr[j]
                subset.append(arr[j])

        # If the sum is 'K'.
        if total_sum == k:
            ans.append(subset)

    # Return ans.
    return ans


def main():
    # Example usage
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    k = 7
    result = findSubsetsThatSumToK(arr, n, k)
    print("Subsets that sum to", k, ":", result)


if __name__ == "__main__":
    main()
