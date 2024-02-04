def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner

    while row < rows and col >= 0:
        current_value = matrix[row][col]

        if current_value == target:
            return True
        elif current_value < target:
            row += 1  # Move down in the matrix
        else:
            col -= 1  # Move left in the matrix

    return False

# Example usage:
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = search_matrix(matrix, target)
print(result)  # Output: True
