"""
@author: Infinixor
"""

# Function to check if the coloring is valid
def isCorrect(mat, cur, color, col):
    # Iterate through each cell
    for i in range(len(mat)):
        # Check if (i, j) is not valid
        if mat[cur][i] == 1 and color[i] == col:
            return False
    # Return true as all cells are valid        
    return True


# Function to check if entire graph is colored correctly
def graphCol(mat, m, cur, color):
    # If current row is the last row
    if cur == len(mat):
        return True
    # Generate all possible combinations recursively
    for j in range(1, m+1):
        if isCorrect(mat, cur, color, j):
            color[cur] = j
            # If we found a valid coloring, return true
            if graphCol(mat, m, cur + 1, color):
                return True
            color[cur] = 0
    # No valid coloring found
    return False


# Main function to color the graph
def graphColoring(mat, m):
    v = len(mat)
    # Initialize color list
    color = [0] * v
    if graphCol(mat, m, 0, color):
        return "YES"
    return "NO"


def main():
    # Example usage
    adjacency_matrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    max_colors = 3

    result = graphColoring(adjacency_matrix, max_colors)

    if result == "YES":
        print("The graph can be colored using", max_colors, "colors.")
    else:
        print("The graph cannot be colored using", max_colors, "colors.")


if __name__ == "__main__":
    main()
