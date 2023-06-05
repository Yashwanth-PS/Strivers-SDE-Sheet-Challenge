def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    # Determine the dimensions of the matrix
    m = len(matrix)
    n = len(matrix[0])

    # Variables to track if first row and first column need to be set to 0
    first_row_zero = False
    first_col_zero = False

    # Check if first row and first column contain 0's
    for i in range(n):
        if matrix[0][i] == 0:
            first_row_zero = True
            break

    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Use first row and first column to mark rows and columns to be set to 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set rows and columns to 0 based on first row and first column markings
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(n):
                matrix[i][j] = 0

    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0

    # Set first row and first column to 0 if necessary
    if first_row_zero:
        for i in range(n):
            matrix[0][i] = 0

    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

    return matrix