from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

"""
@author:  Infinixor 

"""
def calculateMinPlatforms(at, dt, n):
    platforms = [0 for _ in range(2361)]
    minNumOfPlatforms = 1

    for i in range(n):
        platforms[at[i]] += 1
        platforms[dt[i] + 1] -= 1

    for i in range(1, 2361):
        platforms[i] = platforms[i] + platforms[i - 1]
        minNumOfPlatforms = max(minNumOfPlatforms, platforms[i])

    return minNumOfPlatforms

def main():
    # Test case 1
    at1 = [900, 940, 950, 1100, 1500, 1800]
    dt1 = [910, 1200, 1120, 1130, 1900, 2000]
    n1 = 6
    minPlatforms1 = calculateMinPlatforms(at1, dt1, n1)
    print("Minimum number of platforms required for test case 1:", minPlatforms1)

    # Test case 2
    at2 = [900, 940, 950, 1100, 1500]
    dt2 = [910, 1200, 1120, 1130, 1900]
    n2 = 5
    minPlatforms2 = calculateMinPlatforms(at2, dt2, n2)
    print("Minimum number of platforms required for test case 2:", minPlatforms2)

def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

if __name__ == "__main__":
    main()
