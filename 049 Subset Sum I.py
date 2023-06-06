class Solution:
    def subsetSums(self, arr):
        N = len(arr)
        res = []
        self.helper(0, 0, N, arr, res)
        res.sort()
        return res
        
    def helper(self, ind, S, N, arr, res):
        if ind == N:
            res.append(S)
            return
        self.helper(ind + 1, S + arr[ind], N, arr, res)
        self.helper(ind + 1, S, N, arr, res)

def main():
    # Test case
    array = [1, 2, 3]
    solution = Solution()
    result = solution.subsetSums(array)
    print("Subset Sums for array [1, 2, 3]:", result)

if __name__ == '__main__':
    main()
