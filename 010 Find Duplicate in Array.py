"""
@author:  Infinixor 

"""
def findDuplicate(nums, n):
    tortoise, hare = nums[0], nums[nums[0]]
    while tortoise != hare:
        tortoise, hare = nums[tortoise], nums[nums[hare]]
    
    tortoise = 0
    while tortoise != hare:
        tortoise, hare = nums[tortoise], nums[hare]
    
    return tortoise

def main():
    # Test case 1
    nums1 = [1, 3, 4, 2, 2]
    n1 = 5
    result1 = findDuplicate(nums1, n1)
    print("Duplicate in nums1:", result1)

    # Test case 2
    nums2 = [3, 1, 3, 4, 2]
    n2 = 5
    result2 = findDuplicate(nums2, n2)
    print("Duplicate in nums2:", result2)

if __name__ == '__main__':
    main()
