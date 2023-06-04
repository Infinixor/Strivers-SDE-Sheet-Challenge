def maxSubarraySum(arr, n):
    max_sum = 0
    current_sum = 0

    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def main():
    # Test Case 1
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(arr)
    print(f"Array: {arr}")
    max_sum = maxSubarraySum(arr, n)
    print(f"Max Subarray Sum: {max_sum}")
    print()

    # Test Case 2
    arr = [1, 2, 3, 4, -10]
    n = len(arr)
    print(f"Array: {arr}")
    max_sum = maxSubarraySum(arr, n)
    print(f"Max Subarray Sum: {max_sum}")
    print()

    # Test Case 3
    arr = [-1, -2, -3, -4, -5]
    n = len(arr)
    print(f"Array: {arr}")
    max_sum = maxSubarraySum(arr, n)
    print(f"Max Subarray Sum: {max_sum}")
    print()


if __name__ == "__main__":
    main()
