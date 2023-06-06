class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort()
        ds = []
        self.findcombinations(candidates, target, 0, [], ans)
        return ans

    def findcombinations(self, arr, target, ind, ds, ans):
        if target == 0:
            ans.append(ds.copy())
            return
        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i - 1]:
                continue
            if arr[i] > target:
                break
            ds.append(arr[i])
            self.findcombinations(arr, target - arr[i], i + 1, ds, ans)
            ds.pop()

def main():
    # Test case 1
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    solution = Solution()
    result1 = solution.combinationSum2(candidates1, target1)
    print("Combination Sum 2 for target 8 and candidates1:")
    for combination in result1:
        print(combination)
    print()

    # Test case 2
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    result2 = solution.combinationSum2(candidates2, target2)
    print("Combination Sum 2 for target 5 and candidates2:")
    for combination in result2:
        print(combination)
    print()

if __name__ == '__main__':
    main()
