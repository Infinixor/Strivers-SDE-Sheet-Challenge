"""
@author: Infinixor
"""

from collections import deque

def longestSubSeg(arr, n, k):
    # Starting index of array under consideration.
    l = 0
    max_len = 0
    q = deque()
    # To store current size of the queue.
    size = 0

    # i decides current ending point, i.e. the right pointer.
    for r in range(n):
        if (arr[r] == 0):
            q.append(r)
            size += 1

        # Updating queue when its size becomes greater than k.
        if (size > k):
            # Updating starting index of array under consideration.
            l = q.popleft() + 1
            size -= 1

        max_len = max(max_len, r - l + 1)

    return max_len


def main():
    # Example usage
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
    n = len(arr)
    k = 2
    result = longestSubSeg(arr, n, k)
    print("Maximum length of subarray with at most", k, "replacements:", result)


if __name__ == "__main__":
    main()
