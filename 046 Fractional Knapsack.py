"""
@author: Infinixor
"""

# Comparator to sort items.
def compare(a):
    return a[1] / a[0]


def maximumValue(items, n, w):
    # Sort items according to value/weight.
    items = sorted(items, key=compare, reverse=True)

    maxValue = 0
    currWeight = 0

    for i in range(n):
        if currWeight + items[i][0] <= w:
            currWeight += items[i][0]
            maxValue += items[i][1]

        else:
            remainingWeight = w - currWeight

            # Pick a fraction of the current item.
            maxValue += items[i][1] * (remainingWeight / items[i][0])
            break

    return round(maxValue, 2)


def main():
    # Example usage
    items = [(10, 60), (40, 40), (20, 100), (30, 120)]
    n = len(items)
    w = 50
    result = maximumValue(items, n, w)
    print("Maximum value that can be obtained with a weight of", w, ":", result)


if __name__ == "__main__":
    main()
