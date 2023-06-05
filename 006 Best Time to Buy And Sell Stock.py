def maximumProfit(prices):
    maxprofit = 0
    minele = float("inf")
    for i in range(len(prices)):
        minele = min(prices[i], minele)
        maxprofit = max(prices[i] - minele, maxprofit)
    return maxprofit


def main():
    # Test Case 1
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices}")
    max_profit = maximumProfit(prices)
    print(f"Maximum Profit: {max_profit}")
    print()

    # Test Case 2
    prices = [7, 6, 4, 3, 1]
    print(f"Prices: {prices}")
    max_profit = maximumProfit(prices)
    print(f"Maximum Profit: {max_profit}")
    print()

    # Test Case 3
    prices = [1, 2, 3, 4, 5]
    print(f"Prices: {prices}")
    max_profit = maximumProfit(prices)
    print(f"Maximum Profit: {max_profit}")
    print()


if __name__ == "__main__":
    main()
