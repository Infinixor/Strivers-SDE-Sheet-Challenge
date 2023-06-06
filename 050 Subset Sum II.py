class Solution:
    def subsetsWithDup(self, nums) :
        nums = sorted(nums)
        res = []
        self.backtracking(res, 0, [], nums)
        return res
    
    def backtracking(self, res, start, subset, nums):
        res.append(list(subset))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.backtracking(res, i + 1, subset, nums)
            subset.pop()

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 2]
    result1 = solution.subsetsWithDup(nums1)
    print("Test case 1:")
    print("Expected output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]")
    print("Actual output:", result1)
    print()

    # Test case 2
    nums2 = [1, 2, 3]
    result2 = solution.subsetsWithDup(nums2)
    print("Test case 2:")
    print("Expected output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]")
    print("Actual output:", result2)
