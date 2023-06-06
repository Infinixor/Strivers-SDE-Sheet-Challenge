class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isTerminal = False


def insert(root, word):
    curr = root
    for i in range(len(word)):
        if curr.children[ord(word[i]) - ord('a')] is None:
            curr.children[ord(word[i]) - ord('a')] = TrieNode()
        curr = curr.children[ord(word[i]) - ord('a')]
    curr.isTerminal = True


def search(root, s, res, temp, pos):
    curr = root
    for i in range(pos, len(s)):
        if curr.children[ord(s[i]) - ord('a')] is None:
            return
        if curr.children[ord(s[i]) - ord('a')].isTerminal:
            lastWord = temp + s[pos: i + 1]
            if i == len(s) - 1:
                res.append(lastWord)
            else:
                search(root, s, res, lastWord + " ", i + 1)
        curr = curr.children[ord(s[i]) - ord('a')]


def wordBreak(s, dictionary):
    root = TrieNode()
    for word in dictionary:
        insert(root, word)
    res = []
    search(root, s, res, "", 0)
    return res


if __name__ == "__main__":
    # Test case 1
    s1 = "catsanddog"
    dictionary1 = ["cat", "cats", "and", "sand", "dog"]
    result1 = wordBreak(s1, dictionary1)
    print("Test case 1:")
    print("Expected output: ['cat sand dog', 'cats and dog']")
    print("Actual output:", result1)
    print()

    # Test case 2
    s2 = "pineapplepenapple"
    dictionary2 = ["apple", "pen", "applepen", "pine", "pineapple"]
    result2 = wordBreak(s2, dictionary2)
    print("Test case 2:")
    print("Expected output: ['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple']")
    print("Actual output:", result2)
