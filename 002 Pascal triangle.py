"""
@author:  Infinixor 

"""
def printPascal(n: int):
    triangle = []
    for line in range(0, n):
        current_line = []
        for i in range(0, line + 1):
            if i == 0 or i == line:
                current_line.append(1)
            else:
                current_line.append(triangle[line - 1][i - 1] + triangle[line - 1][i])
        triangle.append(current_line)

    return triangle


def main():
    test_cases = [5, 7, 10]
    for n in test_cases:
        pascal_triangle = printPascal(n)
        print(f"Pascal Triangle for n = {n}:")
        for line in pascal_triangle:
            print(line)
        print()


if __name__ == "__main__":
    main()
