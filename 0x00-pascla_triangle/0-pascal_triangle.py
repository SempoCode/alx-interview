def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list: A list of lists, where each sublist represents a row of Pascal's Triangle.

    The function returns an empty list if n <= 0.
    Example:
    pascal_triangle(5) returns:
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the first row of Pascal's Triangle
    triangle = [[1]]  # The first row is always [1]

    # Loop to generate each row from the 2nd to the nth
    for i in range(1, n):
        # Start each new row with 1
        row = [1]
        
        # Calculate the values for the middle of the row
        # Each value is the sum of the two numbers above it
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # End each row with 1
        row.append(1)
        
        # Append the new row to the triangle
        triangle.append(row)

    return triangle
