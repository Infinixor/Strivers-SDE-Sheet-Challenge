"""
@author: Infinixor
"""

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    coinsCount = 0
    n = len(denominations)

    # Pick coins in decreasing order of their values
    for i in range(n - 1, -1, -1):
        coinsCount += amount // denominations[i]
        amount %= denominations[i]

    return coinsCount


def main():
    # Example usage
    amount = 1278
    result = findMinimumCoins(amount)
    print("Minimum number of coins required to make", amount, ":", result)


if __name__ == "__main__":
    main()

