"""
@author:  Infinixor 

"""

def sort012(nums, n):
    hi = len(nums) - 1
    lo = 0
    mid = 0
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            mid += 1
            lo += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1


def main():
    # Test Case 1
    nums = [2, 0, 2, 1, 1, 0]
    n = len(nums)
    print(f"Original Array: {nums}")
    sort012(nums, n)
    print(f"Sorted Array: {nums}")
    print()

    # Test Case 2
    nums = [0, 1, 2, 0, 1, 2]
    n = len(nums)
    print(f"Original Array: {nums}")
    sort012(nums, n)
    print(f"Sorted Array: {nums}")
    print()

    # Test Case 3
    nums = [1, 0, 2]
    n = len(nums)
    print(f"Original Array: {nums}")
    sort012(nums, n)
    print(f"Sorted Array: {nums}")
    print()


if __name__ == "__main__":
    main()
