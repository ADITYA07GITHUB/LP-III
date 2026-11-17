
n = int(input("Enter number of queens: "))

board = [[0] * n for _ in range(n)]

def isSafe(row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(col):
    if col == n:
        return True

    for row in range(n):
        if isSafe(row, col):
            board[row][col] = 1

            if solve(col + 1):
                return True

            board[row][col] = 0

    return False

if n > 0 and solve(0):
    print("Solution:")
    for row in board:
        print(*row)
else:
    print("No solution exists")
###time complexity of n queen problem is O(n!) and space complexity is O(n^2)


# N-Queens Python Code – Line-by-Line Explanation
# I'll explain the Python code in very simple language, so you can understand it and explain it in your DAA practical viva.
# 1. Take input and create chessboard
# n = int(input("Enter number of queens: "))board = [[0] * n for _ in range(n)]



# Explanation:
# - input() takes the number of queens from the user.
# - int() converts the input into an integer.
# - board creates an N×N chessboard.
# - 0 means the position is empty.
# - 1 means a queen is placed.
# For example, if n = 4, the board looks like:
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0


# 2. isSafe() Function
# This function checks whether placing a queen at a given position is safe.
# def isSafe(row, col):



# Here:
# - row = Row number.
# - col = Column number.
# A. Check left side of the row
# for i in range(col):    if board[row][i] == 1:        return False



# Explanation:
# - range(col) checks all columns before the current column.
# - board[row][i] == 1 checks whether another queen exists in that row.
# - If a queen is found, return False.
# Why check only the left side?

# Because we place queens from left to right, one column at a time.
# B. Check upper-left diagonal
# for i, j in zip(range(row, -1, -1),                range(col, -1, -1)):    if board[i][j] == 1:        return False



# Explanation:
# - i represents the row.
# - j represents the column.
# - zip() combines the row and column positions.
# - range(row, -1, -1) moves upward.
# - range(col, -1, -1) moves leftward.
# If another queen exists on the upper-left diagonal, return False.
# C. Check lower-left diagonal
# for i, j in zip(range(row, n),                range(col, -1, -1)):    if board[i][j] == 1:        return False



# Explanation:
# - range(row, n) moves downward.
# - range(col, -1, -1) moves leftward.
# - zip() combines the positions.
# If another queen is found on the lower-left diagonal, return False.
# D. Return True
# return True



# If no queen is found in any of these directions, the position is safe.
# 3. solve() Function – Main Backtracking Logic
# def solve(col):



# This function places queens column by column using recursion.
# A. Base condition
# if col == n:    return True



# Explanation:

# When col == n, it means all N queens have been successfully placed.

# For n = 4, the columns are 0, 1, 2 and 3. Reaching column 4 means all four queens have been placed.
# B. Try every row
# for row in range(n):



# This loop tries placing a queen in each row of the current column.

# For example, when n = 4:
# row = 0
# row = 1
# row = 2
# row = 3


# C. Check and place queen
# if isSafe(row, col):    board[row][col] = 1



# Explanation:
# - isSafe() checks whether the position is safe.
# - If safe, board[row][col] = 1 places the queen.
# D. Recursive call
# if solve(col + 1):    return True



# Explanation:

# After placing a queen, the function calls itself to place another queen in the next column.

# For example:
# solve(0) → First queen
# solve(1) → Second queen
# solve(2) → Third queen
# solve(3) → Fourth queen
# solve(4) → All queens placed


# E. Backtracking
# board[row][col] = 0



# This is the most important line for your viva.

# Suppose you place a queen, but later you cannot place the next queen safely.

# The algorithm removes the previously placed queen by changing 1 back to 0.

# Then it tries another row.

# This process is called backtracking.
# F. Return False
# return False



# If no row is safe in the current column, the function returns False to the previous recursive call.

# 4. Print the Solution
# if n > 0 and solve(0):    print("Solution:")    for row in board:        print(*row)else:    print("No solution exists")



# Explanation:
# - n > 0 checks that the input is positive.
# - solve(0) starts placing queens from the first column.
# - for row in board prints each row.
# - print(*row) prints the values separated by spaces.
# - If no arrangement is possible, it prints "No solution exists".
# 5. Dry Run for N = 4
# Final valid arrangement

# ♛






# ♛

# ♛






# ♛



# Each row and column has exactly one queen, and no two queens share a diagonal.
# The algorithm may first try placing the queen at row 0, column 0. If this choice eventually fails, it removes that queen and tries another row.

# One successful arrangement is:
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0


# 6. Time and Space Complexity
# Complexity	Explanation
# Time	O(N × N!) upper bound for this implementation, because safety checks take O(N)
# Space	O(N²) for the chessboard
# Recursion stack	O(N)

# 7. How to Explain This Code in Viva
# You can speak this answer:
# "Sir, this program solves the N-Queens problem using backtracking. First, we take the number of queens from the user and create an N×N chessboard. Then the isSafe function checks the left row, upper-left diagonal and lower-left diagonal. The solve function places queens column by column using recursion. If a queen cannot be placed, we remove the previous queen and try another position. This process is called backtracking. When all N queens are placed safely, we print the solution."

# Most important viva question: Why do we write board[row][col] = 0?

# Answer: To remove the previously placed queen when that position does not lead to a solution, allowing us to try another position.