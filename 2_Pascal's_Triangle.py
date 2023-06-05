def printPascal(n:int):
    # Write your code here.
    ans = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize each row with 1s
        if i > 1:
            for j in range(1, i):  # Exclude the first and last elements
                # Calculate value based on the row above
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]  
        ans.append(row)
    return ans # Return a list of lists.