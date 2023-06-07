def subarraysXor(arr, x):
    n = len(arr)
    # To store the prefix XOR's.
    prefXor = {}
    ans = 0
    # To keep track of the current xor.
    currXor = 0
    # Initially, XOR is 0.
    prefXor[0] = 1
    for i in range(n):
        # Update the XOR of the current prefix.
        currXor = currXor ^ arr[i]
        # Required value of the prefix XOR to make the XOR of the subarray equal to X.
        req = x ^ currXor
        if req in prefXor:
            # Add the count of prefix arrays with the required XOR.
            ans += prefXor[req]
        if currXor in prefXor:
            prefXor[currXor] = prefXor[currXor] + 1
        else: 
            prefXor[currXor] = 1
    return ans


if __name__ == "__main__":
    # Test case 1
    arr1 = [4, 2, 2, 6, 4]
    x1 = 6
    result1 = subarraysXor(arr1, x1)
    print("Test case 1:")
    print("Expected output: 4")
    print("Actual output:", result1)
    print()

    # Test case 2
    arr2 = [5, 6, 7, 8, 9]
    x2 = 5
    result2 = subarraysXor(arr2, x2)
    print("Test case 2:")
    print("Expected output: 2")
    print("Actual output:", result2)
