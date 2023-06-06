class Solution:
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)
        
    def isPal(self, s):
        return s == s[::-1]

def main():
    # Test case
    string = "aab"
    solution = Solution()
    result = solution.partition(string)
    print("Palindrome Partitioning for string 'aab':")
    for partition in result:
        print(partition)
    print()

if __name__ == '__main__':
    main()
